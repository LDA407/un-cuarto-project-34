from django.contrib import admin
from .models import (
    MetaElements,
    SocialLinks, Contact,
    HeroSettings, ShowReel,
    ServicesSection, Services,
    PortafolioSection, Portafolio,
    AboutUsSection, Team, Comment,Galeria, GaleriaSection, TeamSection,
GaleriaSection
)


admin.site.register(GaleriaSection)
admin.site.register(Galeria)
admin.site.register(MetaElements)
admin.site.register(SocialLinks)
admin.site.register(Contact)
admin.site.register(HeroSettings)
admin.site.register(ShowReel)
admin.site.register(ServicesSection)
admin.site.register(Services)
admin.site.register(PortafolioSection)
admin.site.register(Portafolio)
admin.site.register(Comment)
admin.site.register(AboutUsSection)
admin.site.register(TeamSection)
admin.site.register(Team)