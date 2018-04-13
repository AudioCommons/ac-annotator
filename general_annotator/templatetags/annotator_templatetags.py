from django import template

register = template.Library()


@register.filter()
def fs_embed_large(value):
    embed_code = '<iframe frameborder="0" scrolling="no" src="https://www.freesound.org/embed/sound/iframe/{0}/simple/large_no_info/?spec=1&td=1" width="920" height="245"></iframe>'
    return embed_code.format(str(value))
