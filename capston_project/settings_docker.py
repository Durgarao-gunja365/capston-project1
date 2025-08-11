from .settings import *  # import all base settings

# Disable debug mode
DEBUG = False

# Allowed hosts
ALLOWED_HOSTS = ['*']

# Static files location
STATIC_ROOT = BASE_DIR / "staticfiles"

# Use WhiteNoise to serve static files efficiently
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Template caching for speed
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

# Simple in-memory cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
