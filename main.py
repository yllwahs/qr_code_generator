import qrcode
img = qrcode.make('GitHub Webhook')
img.save("github_webhook.png")
