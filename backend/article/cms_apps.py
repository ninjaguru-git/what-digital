from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class ArticleApphook(CMSApp):
    """Article App hook."""
    app_name = "article"
    name = "Article Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["backend.article.urls"]