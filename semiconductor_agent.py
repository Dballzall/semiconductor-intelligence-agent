"""
Semiconductor Intelligence Agent - Production Version
Runs automatically via GitHub Actions
"""

import os
import requests
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Get credentials from environment variables (set in GitHub Secrets)
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD')
RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')

# Search queries
SEARCH_QUERIES = {
    'companies': 'TSMC NVIDIA Intel Samsung AMD ASML semiconductor',
    'policy': 'semiconductor CHIPS Act export controls trade',
    'supply_chain': 'chip shortage semiconductor supply chain manufacturing'
}

def search_news(query, max_results=5):
    """Search for recent news"""
    url = "https://newsapi.org/v2/everything"
    
    # Calculate strictly the last 24 hours
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    params = {
        'q': query,
        'apiKey': NEWS_API_KEY,
        'language': 'en',
        'sortBy': 'publishedAt', # This ensures you get NEWEST, not "most popular"
        'pageSize': max_results,
        'from': yesterday.strftime('%Y-%m-%d'),
        'to': today.strftime('%Y-%m-%d')
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        articles = []
        for article in data.get('articles', []):
            articles.append({
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'url': article.get('url', ''),
                'source': article.get('source', {}).get('name', '')
            })
        
        print(f"  ✓ Found {len(articles)} articles")
        return articles
        
    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        return []


def analyze_with_claude(news_data):
    """Use Claude to analyze news"""
    news_text = "# Semiconductor Industry News - Past 24 Hours\n\n"
    
    for category, articles in news_data.items():
        if articles:
            news_text += f"\n## {category.upper().replace('_', ' ')}\n\n"
            for article in articles:
                news_text += f"**{article['title']}** ({article['source']})\n"
                news_text += f"{article['description']}\n"
                news_text += f"Link: {article['url']}\n\n"
    
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    
    prompt = f"""You are a semiconductor industry analyst creating an executive briefing for corporate communications professionals.

Analyze this news and create a concise, actionable briefing:

{news_text}

Format your response as:

📊 EXECUTIVE SUMMARY
[2-3 sentence overview of the week]

🔑 KEY DEVELOPMENTS
[3-5 bullet points of most important news]

📋 POLICY & REGULATION
[Any significant policy changes or regulatory news]

⛓️ SUPPLY CHAIN
[Supply chain developments, shortages, or manufacturing news]

💡 COMMUNICATIONS IMPLICATIONS
[What corporate comms teams should know or monitor]

Keep it concise, professional, and actionable."""

    data = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 2000,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['content'][0]['text']
    except Exception as e:
        return f"Error calling Claude API: {str(e)}"

def send_email(subject, body):
    """Send email briefing"""
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        
        msg.attach(MIMEText(body, 'plain'))
        
        html = f"""
        <html>
          <body style="font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px;">
            <h2 style="color: #2c3e50;">🔬 Semiconductor Industry Intelligence Brief</h2>
            <p style="color: #7f8c8d;">{datetime.now().strftime('%B %d, %Y')}</p>
            <hr style="border: 1px solid #ecf0f1;">
            <div style="white-space: pre-wrap; line-height: 1.6;">{body}</div>
            <hr style="border: 1px solid #ecf0f1; margin-top: 30px;">
            <p style="color: #95a5a6; font-size: 11px;">
              Generated automatically by your AI Intelligence Agent
            </p>
          </body>
        </html>
        """
        msg.attach(MIMEText(html, 'html'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        print("✓ Email sent successfully")
        return True
        
    except Exception as e:
        print(f"✗ Error sending email: {str(e)}")
        return False

def main():
    """Main execution"""
    print("=" * 70)
    print("SEMICONDUCTOR INTELLIGENCE AGENT")
    print(f"Running at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 70)
    print()
    
    # Gather news
    print("📰 Step 1: Gathering news...")
    news_data = {}
    
    for category, query in SEARCH_QUERIES.items():
        print(f"  Searching {category}...")
        news_data[category] = search_news(query)
    
    print()
    
    # Analyze
    print("🤖 Step 2: Analyzing with Claude AI...")
    briefing = analyze_with_claude(news_data)
    print("✓ Analysis complete")
    print()
    
    # Send email
    print("📧 Step 3: Sending email briefing...")
    subject = f"Semiconductor Industry Brief - {datetime.now().strftime('%B %d, %Y')}"
    
    if send_email(subject, briefing):
        print()
        print("=" * 70)
        print("✅ SUCCESS! Briefing sent.")
        print("=" * 70)
    else:
        print()
        print("=" * 70)
        print("❌ Failed to send email. Briefing content:")
        print("=" * 70)
        print(briefing)

if __name__ == "__main__":
    main()
