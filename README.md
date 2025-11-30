# Semiconductor Intelligence Agent

**What Is It: An AI-powered agent that monitors the semiconductor industry and delivers automated daily briefings to your inbox.**

Built for corporate communications professionals who need to stay informed without drowning in news feeds.

---

## What It Does

This AI agent:
- **Searches** semiconductor industry news across major publications
- **Analyzes** headlines using Claude AI to identify key developments
- **Delivers** a professional executive briefing to your email
- **Runs automatically** every morning at 8 AM (no manual work required)

### What It Monitors

- **Major Companies**: TSMC, NVIDIA, Intel, Samsung, AMD, ASML
- **Policy & Regulation**: Export controls, CHIPS Act, trade policy
- **Supply Chain**: Chip shortages, manufacturing, capacity

---
<img width="868" height="545" alt="Screenshot 2025-11-29 at 9 32 28 PM" src="https://github.com/user-attachments/assets/f5c99eec-76c2-43e1-9886-a15fdd8fde53" />

## Sample Briefing

Here's what you get in your inbox every morning:

```
EXECUTIVE SUMMARY

KEY DEVELOPMENTS

POLICY & REGULATION

SUPPLY CHAIN

COMMUNICATIONS IMPLICATIONS
```

---

## 🚀 Quick Start (5 Minutes)

### What You'll Need (All Free)

1. **Anthropic API Key** - Get it at [console.anthropic.com](https://console.anthropic.com)
   - Free tier: $5 in credits (enough for months)
   
2. **NewsAPI Key** - Get it at [newsapi.org](https://newsapi.org/register)
   - Free tier: 100 requests/day
   
3. **Gmail App Password** - Create at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - Requires 2-factor authentication enabled
   - Name it "semiconductor-agent"

## Automated Daily Execution (Build the Agent here)

**Fork this repository and set it up to run automatically:**

#### Step 1: Fork This Repo
- Click "Fork" at the top of this page
- You now have your own copy

#### Step 2: Add Your API Keys as Secrets
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add each of these secrets:

| Secret Name | Value |
|------------|-------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key (starts with `sk-ant-`) |
| `NEWS_API_KEY` | Your NewsAPI key |
| `SENDER_EMAIL` | Your Gmail address |
| `SENDER_PASSWORD` | Your Gmail app password (16 characters) |
| `RECIPIENT_EMAIL` | Your Gmail address (same as sender) |

#### Step 3: Enable GitHub Actions
1. Go to **Actions** tab
2. Click "I understand my workflows, go ahead and enable them"
3. Click **Daily Semiconductor Briefing** on the left
4. Click **Run workflow** → **Run workflow** (to test it now)

#### Step 4: Done!
- Your agent now runs automatically every day at 8 AM Eastern
- Check the **Actions** tab to see run history
- Check your email for the briefing

---

## ⚙️ Customization

### Change the Topics

Edit `semiconductor_agent.py` to monitor different topics:

```python
SEARCH_QUERIES = {
    'companies': 'TSMC NVIDIA Intel Samsung AMD ASML semiconductor',
    'policy': 'semiconductor CHIPS Act export controls trade',
    'supply_chain': 'chip shortage semiconductor supply chain',
    'ai_chips': 'AI accelerator GPU tensor processing',  # ADD NEW TOPICS
    'manufacturing': 'fab construction ASML lithography'  # LIKE THESE
}
```

### Change the Time

Edit `.github/workflows/daily-briefing.yml`:

```yaml
on:
  schedule:
    - cron: '0 13 * * *'  # 8 AM Eastern = 13:00 UTC
```

Common times (in UTC):
- 8 AM Eastern: `'0 13 * * *'`
- 9 AM Eastern: `'0 14 * * *'`
- 7 AM Pacific: `'0 15 * * *'`

### Add More Email Recipients

Edit `semiconductor_agent.py` to send to multiple people:

```python
RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')
CC_EMAILS = "colleague1@company.com,colleague2@company.com"
```

---

## Cost

**Essentially free:**

- **Anthropic API**: ~$0.03-0.05 per briefing = **~$1.50/month**
- **NewsAPI**: Free tier (100 requests/day)
- **Gmail**: Free
- **GitHub Actions**: Free (2,000 minutes/month on free tier)

**Total: About $1.50/month** for daily AI-powered briefings.

---

## How It Works

```
┌─────────────────┐
│  GitHub Actions │  ← Runs daily at 8 AM
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   NewsAPI       │  ← Searches semiconductor news
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Claude AI      │  ← Analyzes and summarizes
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Your Inbox     │  ← Receives briefing
└─────────────────┘
```

The workflow:
1. GitHub Actions triggers at scheduled time
2. Script searches NewsAPI for semiconductor-related articles
3. Claude AI analyzes the articles and creates an executive summary
4. Formatted briefing is emailed to you
5. Repeat tomorrow

---

## Security

- API keys are stored as GitHub Secrets (encrypted)
- Never commit API keys to the repository
- Gmail app passwords are separate from your main password
- All code runs in isolated GitHub Actions containers

---

## Use Cases Beyond Semiconductors

This same agent can monitor ANY industry:

**Examples:**
- **AI/ML Industry**: Track OpenAI, Anthropic, Google AI developments
- **Space Economy**: Monitor SpaceX, Blue Origin, satellite companies
- **Biotech**: Follow FDA approvals, clinical trials, mergers
- **Crypto**: Track regulations, major exchanges, DeFi developments
- **Your Company's Competitors**: Monitor their announcements and news

**Just change the search queries!**

---

## Why I Built This

As a corporate communications professional, I was spending 1-2 hours every morning reading through semiconductor news to stay informed. This agent:

- Saves me **8-10 hours per week**
- Ensures I **never miss important developments**
- Provides **consistent, unbiased analysis**
- Costs less than **one cup of coffee per month**

It's not about replacing communications professionals—it's about augmenting our work with AI so we can focus on strategy instead of information gathering.

---

## Troubleshooting

**"Invalid API key" error:**
- Verify you copied the full key with no spaces
- Anthropic keys start with `sk-ant-`
- Check the key works at console.anthropic.com

**"Authentication failed" email error:**
- Use Gmail app password, not your regular password
- App password is 16 characters
- Ensure 2FA is enabled on your Gmail

**No email received:**
- Check spam folder
- Verify secrets are set correctly in GitHub
- Check Actions tab for error logs

**"Rate limit exceeded":**
- NewsAPI free tier limits to 100 requests/day
- Reduce search queries or upgrade NewsAPI plan

---

## Next Steps

Once you have this running:

1. **Customize the topics** to match your industry focus
2. **Share with your team** (they can fork and use their own API keys)
3. **Build your own agents** for other monitoring tasks
4. **Explore AI automation** for other communications workflows

---

## Learn More

- [Anthropic API Documentation](https://docs.anthropic.com)
- [NewsAPI Documentation](https://newsapi.org/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [My LinkedIn] (https://www.linkedin.com/in/ball-daniel/) - Follow for more AI + comms content

---

## License

MIT License - Free to use, modify, and distribute.

---

## Acknowledgments

Built with:
- [Claude AI](https://claude.ai) by Anthropic
- [NewsAPI](https://newsapi.org)
- [GitHub Actions](https://github.com/features/actions)

---

## Found This Useful?

If this saved you time or inspired you to build your own AI agents, give it a star ⭐ and share it with other communications professionals!

**Questions?** Open an issue or connect with me on LinkedIn.

---
