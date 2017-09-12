from django import template


register = template.Library()


@register.filter()
def fs_embed(value):
    embed_code = '<iframe frameborder="0" scrolling="no" src="https://www.freesound.org/embed/sound/iframe/{0}/simple/medium_no_info/" width="130" height="80"></iframe>'
    return embed_code.format(str(value))
