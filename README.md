# Semiconductor Intelligence Agent

An AI-powered briefing agent that monitors the semiconductor industry (or whatever industry you pick) and delivers a daily executive summary straight to your inbox.

Built for communications professionals who need to answer 'What's the latest on [Topic]?' before their boss asks. Automates the 2 hours of morning reading required to stay smart on your given industry.

**No coding required. Setup takes about 5 minutes.**

## What It Does

This AI agent:
- Searches major publications for semiconductor industry news
- Analyzes developments using Claude AI
- Delivers a polished daily briefing to your email
- Runs automatically every morning at 8 AM Eastern (**Note on Timing:** GitHub Actions is a shared service, so exact timing varies.Your email will typically arrive between 7:50 AM and 8:30 AM depending on server load.)

## What It Monitors

- **Major companies:** TSMC, NVIDIA, Intel, Samsung, AMD, ASML
- **Policy & regulation:** CHIPS Act, export controls, trade policy
- **Supply chain:** manufacturing, fab capacity, chip shortages

![Screenshot](https://github.com/user-attachments/assets/f5c99eec-76c2-43e1-9886-a15fdd8fde53)

## Sample Briefing

Each morning you'll receive something like:
```
EXECUTIVE SUMMARY

KEY DEVELOPMENTS
- Example: TSMC expands 2nm roadmap; implications for U.S. competitiveness

POLICY & REGULATION

SUPPLY CHAIN

COMMUNICATIONS IMPLICATIONS
```

## 🚀 Quick Start (5 Minutes)

You don't need technical experience. If you can copy and paste, you can set this up.

### What You'll Need (All Free)

1. **Anthropic API Key** — https://console.anthropic.com
2. **NewsAPI Key** — https://newsapi.org/register
3. **Gmail App Password** — https://myaccount.google.com/apppasswords
   - Requires 2FA. Important: You must have 2-Step Verification enabled on your Google account for the "App Passwords" option to appear. It will not work with your regular email password.
   - Name it "semiconductor-agent"

### Set Up the Daily Email Agent

#### Step 1: Fork This Repository

Click the **Fork** button (this just means 'Make a Copy' into your own account).

This creates your own copy where your daily agent will run

#### Step 2: Add Your Keys (Securely)

Think of these as "passwords" that let the agent read the news and send your email.

They're stored securely — only you can access them.

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add the following:

| Secret Name | Value |
|-------------|-------|
| `ANTHROPIC_API_KEY` | Your Anthropic key (sk-ant-...) |
| `NEWS_API_KEY` | Your NewsAPI key |
| `SENDER_EMAIL` | Your Gmail address |
| `SENDER_PASSWORD` | Your 16-character Gmail app password |
| `RECIPIENT_EMAIL` | Your email (same or different) |

#### Step 3: Enable the Automation (GitHub Actions)

GitHub Actions is simply a free scheduler that runs the agent for you each morning — nothing to install.

1. Go to the **Actions** tab
2. Click **"I understand…"** to enable workflows
3. Select **Daily Semiconductor Briefing**
4. Click **Run workflow** to test it immediately

#### Step 4: Done ✅

- Runs automatically each day at 8 AM Eastern
- View results anytime in the **Actions** tab
- Check your inbox for your first briefing

## ⚙️ Customization (Optional)

These options are here if you want them. You can skip this section if you only need the default setup.

### Change the Topics
### Option A: Use AI to Rewrite It for Your Industry (Easiest)
   1. Open semiconductor_agent.py and copy the entire code.
   2. Paste it into ChatGPT, Claude, or Gemini with this prompt:
      "I have this Python script that tracks semiconductor news. I want to modify it to track the [INSERT INDUSTRY] industry instead. Please
      give me the updated 'SEARCH_QUERIES' dictionary with the best keywords for my industry."
   3. Copy the new code back into your file.

### Option B: Manually Change the Topics
1. Click on the file named semiconductor_agent.py in the file list above.
2. Click the Pencil Icon (Edit) in the top right corner of the file view.
3. Change the words inside the quotes in the SEARCH_QUERIES section.
4. Click Commit changes (green button) to save.
   
```python
SEARCH_QUERIES = {
    'companies': 'TSMC OR NVIDIA OR Intel OR Samsung OR AMD OR ASML',
    'policy': 'semiconductor AND ("CHIPS Act" OR "export controls" OR trade OR tariff)',
    'supply_chain': '"chip shortage" OR "supply chain" OR manufacturing',
    'ai_chips': '"AI accelerator" OR GPU OR "tensor processing"',
    'manufacturing': '"fab construction" OR ASML OR lithography'
}
```

### Change the Send Time

1. Edit the file .github/workflows/daily-briefing.yml (click the Pencil icon).
2. Look for the line cron: '0 13 * * *'
```yaml
on:
  schedule:
    - cron: '0 13 * * *'  # 8 AM Eastern (13:00 UTC)
```

Need a different time? Use crontab.guru to generate the specific code for your timezone.

### Add CC or Additional Recipients

In semiconductor_agent.py:

```python
CC_EMAILS = "colleague1@company.com,colleague2@company.com"
```

## Cost

Essentially free:
- **Anthropic API:** ~$1.50/month
- **NewsAPI:** Free tier
- **Gmail:** Free
- **GitHub Actions:** Free (2,000 minutes/month)

**Total cost:** About $1.50/month for fully automated daily briefings.

## How It Works

A simple daily workflow:

**GitHub Actions → NewsAPI → Claude AI → Your Inbox**

1. Runs at your scheduled time
2. Searches for semiconductor news
3. Claude analyzes and summarizes
4. Email arrives in your inbox
5. Repeats every morning

## Security

- All API keys are stored as encrypted GitHub Secrets
- Nothing is shared publicly
- Gmail app passwords are separate from your main password
- Code runs in isolated GitHub containers

## Use Cases Beyond Semiconductors

This same agent can track any industry, including:
- AI & machine learning
- Space economy
- Biotech & pharma
- Crypto & fintech
- Competitor monitoring
- Regulatory landscapes

Just change the search queries.

## Why I Built This

As a communications professional, you spend lots of time scanning and analyzing news. This agent now:

- Saves 8–10 hours per week
- Ensures you never miss important developments
- Provides consistent, structured updates
- Costs less than one cup of coffee per month

It's not about replacing comms professionals. It's about giving us time back for deep work. 

## Troubleshooting

**Invalid API key:**
- Double-check your keys
- Anthropic keys start with `sk-ant-`

**Email authentication failed:**
- Use your Gmail app password, not your normal password
- Must be 16 characters

**No email received:**
- Check spam
- Verify secrets are correct
- Check the **Actions** tab for run logs

**NewsAPI rate limit:**
- Free tier allows 100 requests/day
- Reduce the number of searches if needed

## Next Steps

After it's running:
- Customize topics for your industry
- Share with teammates (they can fork and use their own keys)
- Build additional agents for other monitoring tasks
- Expand into AI-driven comms workflows

## Learn More

- [Anthropic Documentation](https://docs.anthropic.com)
- [NewsAPI Documentation](https://newsapi.org/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [My LinkedIn](https://www.linkedin.com/in/ball-daniel/)

## License

MIT License — free to use, modify, and share.

## Acknowledgments

Built with:
- Claude AI
- NewsAPI
- GitHub Actions

---

**Found This Useful?**

Give the repo a ⭐ and share it with other communications professionals.

Questions? Open an issue or reach out on [LinkedIn](https://www.linkedin.com/in/ball-daniel/)
