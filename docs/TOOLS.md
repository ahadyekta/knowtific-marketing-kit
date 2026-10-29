# Optional connections: setup guide

The kit works without these (it asks you for exports), but each connection lets Claude read real data. Add them in Claude Code with `claude mcp add ...` (add `--scope user` to use them in every project, or `--scope project` to share with a project via `.mcp.json`). Check what's connected with `/mcp`.

**Safety:** keep credentials out of git. Ad platform connections can spend money; the kit only reads data and suggests changes unless you explicitly ask it to change a budget or pause something.

---

## 1. DataForSEO (keyword research, rankings, competitors, backlinks, Google Business data)
Pay-as-you-go API (minimum deposit, no monthly fee). Create an account, then copy your API login and password from the API Access page.

Local server (recommended):
```
claude mcp add dfs-mcp --scope user --env DATAFORSEO_USERNAME=your_login --env DATAFORSEO_PASSWORD=your_password -- npx -y dataforseo-mcp-server
```
Windows (if plain `npx` fails):
```
claude mcp add dfs-mcp --scope user --env DATAFORSEO_USERNAME=your_login --env DATAFORSEO_PASSWORD=your_password -- cmd /c npx -y dataforseo-mcp-server
```

Remote server alternative (Base64 of `login:password` as the token; check DataForSEO's current MCP docs for the URL before relying on it):
```
claude mcp add --transport http dfs-mcp https://mcp.dataforseo.com/http --header "Authorization: Basic <base64_token>"
```

## 2. Google Ads (official, read-only)
Needs Python 3.10+, `pipx`, a Google Cloud project with Google Ads API access, and OAuth/Application Default Credentials.
```
claude mcp add google-ads-mcp --scope user --env GOOGLE_PROJECT_ID=your_project --env GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json -- pipx run --spec git+https://github.com/googleads/google-ads-mcp.git google-ads-mcp
```
For manager (MCC) accounts add `--env GOOGLE_ADS_LOGIN_CUSTOMER_ID=1234567890`. Follow Google's guide for creating credentials: developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server

## 3. Google Analytics 4 (official, read-only)
Enable the Google Analytics Admin API and Data API in your Cloud project, then sign in:
```
gcloud auth application-default login --scopes="https://www.googleapis.com/auth/analytics.readonly,https://www.googleapis.com/auth/cloud-platform"
claude mcp add analytics-mcp --scope user -- pipx run analytics-mcp
```
The Google account needs at least Viewer access on each GA4 property.

## 4. Meta Ads (official remote server)
Server URL: `https://mcp.facebook.com/ads`, with Facebook OAuth. You need a Meta app ID (create an app in Meta for Developers). In Claude Code:
```
claude mcp add --transport http --client-id <META_APP_ID> meta-ads https://mcp.facebook.com/ads
```
then run `/mcp` to sign in. (You can also add it in the Claude app as a custom connector.) Follow Meta's "Ads MCP server: get started" guide for the current steps.
**It includes tools that create and activate campaigns.** The access needs `ads_mcp_management` plus `ads_read` or `ads_management`. To keep it read-only, grant **only `ads_read`** (not `ads_management`). Also use a dedicated user, connect only the accounts you need, and set account spending limits.

## 5. Klaviyo (official)
Follow Klaviyo's "Connect to the Klaviyo MCP server" guide (remote server recommended): developers.klaviyo.com/en/docs/klaviyo_mcp_server

## 6. Google Search Console
No official Google MCP at the time of writing (check; this may change). Options: export the Performance report (queries and pages, last 3 and 12 months) and give the CSV to Claude; or use an all-in-one SEO MCP (SE Ranking, SEOMCP) that includes Search Console; or a community GSC server (check its code and permissions before installing).

## 7. PageSpeed Insights (free)
Create an API key in Google Cloud (enable the PageSpeed Insights API). Claude can then call:
`https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<page>&strategy=mobile&key=<key>`
Store the key in an environment variable (e.g. `PAGESPEED_API_KEY`), not in the repo.

## 8. Browser for rendered pages and screenshots
```
claude mcp add playwright --scope user -- npx @playwright/mcp@latest
```
Windows (if plain `npx` fails): `claude mcp add playwright --scope user -- cmd /c npx @playwright/mcp@latest`
Lets `lp-review` and `audit` check pages at mobile width and test forms. Claude in Chrome also works if you use it.

## 9. Paid SEO suites (alternatives to DataForSEO)
Ahrefs, Semrush and SE Ranking have official MCP servers on paid plans. Follow each vendor's guide.

## 10. Call notes
Granola, Fathom and similar note-takers: use their connector if available, or export notes and paste them for `sales-kit` (call-notes mode) and `customer-insights`.

---

### What each skill uses
| Skill | Helpful connections |
|---|---|
| audit | GA4, Google Ads, Meta Ads, Search Console, DataForSEO, PageSpeed, browser |
| seo-plan | DataForSEO (or an SEO suite), Search Console, PageSpeed |
| ads-plan (weekly review) | Meta Ads, Google Ads |
| weekly-report | GA4, Google Ads, Meta Ads, Klaviyo |
| email-flows | Klaviyo |
| lp-review | Browser, PageSpeed |
| customer-insights | DataForSEO (Google reviews), call-note tools |
| outbound | DataForSEO (business listings) |
