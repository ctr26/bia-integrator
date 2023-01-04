import os
import logging

import click
from jinja2 import Environment, FileSystemLoader, select_autoescape

from bia_integrator_core.integrator import load_and_annotate_study


logger = logging.getLogger(os.path.basename(__file__))


env = Environment(
    loader = FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

template = env.get_template("image-landing.html.j2")


def generate_image_page_html(accession_id, image_id):

    bia_study = load_and_annotate_study(accession_id)
    bia_image = bia_study.images[image_id]

    reps_by_type = {
        representation.type: representation
        for representation in bia_image.representations
    }

    # Format physical dimensions to X unit x Y unit x Z unit format before passing on to the template
    psize = None
    if bia_image.attributes.get('PhysicalSizeX'):
        psize = str(bia_image.attributes['PhysicalSizeX']) + ' ' + bia_image.attributes[u'PhysicalSizeXUnit'] + \
            ' x ' + str(bia_image.attributes['PhysicalSizeY']) + ' ' + str(bia_image.attributes['PhysicalSizeYUnit'])
        if bia_image.attributes.get('PhysicalSizeZ'):
            psize += ' x ' + str(bia_image.attributes['PhysicalSizeZ']) + ' ' + str(bia_image.attributes['PhysicalSizeZUnit'])
    
    # Convert image dimensions to X x Y x Z format before passing on to the template
    dims = None
    if bia_image.dimensions :
        dl = bia_image.dimensions.split(',')
        if dl[0].startswith('('):
            dl[0] = dl[0].split('(')[1]
            dl[-1] = dl[-1].split(')')[0]
            dims = dl[-1] + ' x ' + dl[-2] 
            if dl[-3].strip() != '1':
                dims += ' x ' + dl[-3]
        else:
            dims = bia_image.dimensions


    rendered = template.render(study=bia_study, image=bia_image, zarr_uri=reps_by_type["ome_ngff"].uri, psize=psize, dimensions=dims)

    return rendered


@click.command()
@click.argument("accession_id")
@click.argument("image_id")
def main(accession_id, image_id):

    logging.basicConfig(level=logging.INFO)

    rendered = generate_image_page_html(accession_id, image_id)

    print(rendered)




if __name__ == "__main__":
    main()