# Cloudflare Pages Deployment Fix

## Problem
The Cloudflare Pages dashboard is configured with the wrong deploy command (`npx wrangler deploy`) which is for Workers, not Pages.

## Solution

### Fix Cloudflare Dashboard Settings

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Navigate to **Workers & Pages**
3. Select **superthrift** project
4. Go to **Settings** → **Builds & deployments**
5. Update the **Deploy command**:
   - **Option A (Recommended)**: Leave it blank - Cloudflare will auto-detect
   - **Option B**: Set to `npx wrangler pages deploy .`
6. **Build command**: Leave blank (no build needed for static HTML)
7. **Root directory**: Leave as `/` or blank
8. Save changes

### Alternative: Use GitHub Actions Only

Since GitHub Actions is already configured correctly, you can:
1. In Cloudflare dashboard, go to **Settings** → **Builds & deployments**
2. Under **Branch deployments**, disable automatic deployments
3. Rely on GitHub Actions workflow (`.github/workflows/deploy.yml`) which already works correctly

## Verification

After fixing, either:
- Push a new commit to trigger GitHub Actions deployment
- Or manually retry the deployment in Cloudflare dashboard

The deployment should succeed without the "Workers-specific command" error.