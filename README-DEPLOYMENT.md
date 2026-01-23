# Cloudflare Deployment Guides

This guide covers deploying SuperThrift to Cloudflare Pages.

## Option 1: Cloudflare Pages (Recommended for Static Sites)

### Via Cloudflare Dashboard (Easiest)

1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Go to **Pages** section
3. Click **Create a project**
4. Connect your GitHub account and select the `verticalconsulting/superthrift` repository
5. Configure build settings:
   - **Build command**: Leave empty (static site)
   - **Build output directory**: `/`
   - **Root directory**: `/`
6. Click **Save and Deploy**

Your site will be deployed to: `https://superthrift.pages.dev`

### Via Wrangler CLI

1. Install Wrangler:
   ```bash
   npm install -g wrangler
   ```

2. Login to Cloudflare:
   ```bash
   wrangler login
   ```

3. Deploy:
   ```bash
   wrangler pages deploy . --project-name=superthrift
   ```

## Option 2: Cloudflare Workers

If you prefer Workers over Pages:

1. Install Wrangler:
   ```bash
   npm install -g wrangler
   ```

2. Initialize Workers project:
   ```bash
   npm init -y
   npm install --save-dev wrangler
   ```

3. Deploy:
   ```bash
   npx wrangler pages deploy . --project-name=superthrift
   ```

## Custom Domain

After deployment, add a custom domain:

1. In Cloudflare Dashboard, go to your Pages project
2. Click **Custom domains**
3. Add your domain (e.g., `superthrift.com`)
4. Follow DNS configuration instructions

## Environment Variables (if needed)

If you need to add form handling or API integrations:

1. Go to **Settings** > **Environment variables**
2. Add your variables for production/preview environments

## Automatic Deployments

Cloudflare Pages automatically deploys when you push to the main branch on GitHub.

## Troubleshooting

- If assets aren't loading, check that paths in HTML are relative (not absolute)
- For 404 errors, ensure `index.html` is in the root directory
- Check build logs in Cloudflare Dashboard for any errors
