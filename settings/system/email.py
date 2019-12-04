from .default import env

EMAIL_CONFIG = env.email_url('EMAIL_URL', default='dummymail://')
vars().update(EMAIL_CONFIG)
