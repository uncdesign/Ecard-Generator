SITE_URL = 'http://localhost'  # Used to generate urls for web version emails, no trailing slash

ADMINS = (
	('Chris Johnson', 'chrisltd@unc.edu'),
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(SITE_ROOT, 'test.db')            # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'testimages')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/testimages/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'uo@n8-_2on%aggtsc-^2(x9z*e*x85u4$=k7_4-*y$v0=0z!&4'



TEMPLATE_DIRS = (
	os.path.join(SITE_ROOT, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


#EMAIL_BACKEND = 'django.core.mail.backends.filebased'
#EMAIL_FILE_PATH = 'test-emails.txt' # change this to a proper location
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'

# Check email output by opening local smtp server in shell: python -m smtpd -n -c DebuggingServer localhost:1025
