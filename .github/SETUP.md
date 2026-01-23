# GitHub Actions Setup for Cloudflare Pages

This repository is configured for automated deployment to Cloudflare Pages via GitHub Actions.

## Setup Steps

### 1. Get Cloudflare Credentials

1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Go to **My Profile** > **API Tokens**
3. Click **Create Token**
4. Use the **Edit Cloudflare Workers** template or create custom token with:
   - Permissions: `Account.Cloudflare Pages — Edit`
   - Account Resources: `Include — Your Account`
5. Copy the API Token

6. Get your Account ID:
   - Go to **Pages** in Cloudflare Dashboard
   - Click any project or create a new one
   - Your Account ID is shown in the URL or project settings

### 2. Add GitHub Secrets

1. Go to your GitHub repository: https://github.com/CLHdevOps/superthrift
2. Click **Settings** > **Secrets and variables** > **Actions**
3. Click **New repository secret** and add:

   **Secret 1:**
   - Name: `CLOUDFLARE_API_TOKEN`
   - Value: Your API token from step 1

   **Secret 2:**
   - Name: `CLOUDFLARE_ACCOUNT_ID`
   - Value: Your Cloudflare Account ID

### 3. Create Cloudflare Pages Project (First Time Only)

Before the first automated deployment, create the project manually:

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/) > **Pages**
2. Click **Create a project** > **Direct Upload**
3. Name it: `superthrift`
4. Click **Create project**
5. You can close the upload page - GitHub Actions will handle deployments

### 4. Test Automated Deployment

Once secrets are added, push any change to trigger deployment:

```bash
git push origin main
```

Go to **Actions** tab in GitHub to see the deployment progress.

## What Happens Automatically

- ✅ Every push to `main` branch deploys to production
- ✅ Every pull request creates a preview deployment
- ✅ Deployments appear in Cloudflare Pages dashboard
- ✅ Automatic SSL certificates
- ✅ Global CDN distribution

## View Deployments

- **GitHub**: Repository > Actions tab
- **Cloudflare**: Dashboard > Pages > superthrift

## Your Site URL

After first deployment: `https://superthrift.pages.dev`

## Troubleshooting

### Deployment Fails
- Verify secrets are set correctly in GitHub
- Check that Cloudflare project name matches `superthrift`
- Ensure API token has proper permissions

### Project Not Found
- Create the Pages project manually first (step 3 above)
- Ensure project name is exactly `superthrift`
