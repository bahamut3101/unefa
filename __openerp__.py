{
    'name':'Estudiantes Unefa',
    'version': '1.0',
    'depends': ['base_setup'],
    'author': 'IRP unefa (Comunidad Bachaco.ve)',
    'category': '',
    'description': """
    Nuestro primer modulo de estudiantes unefa
    """,
    'update_xml': [],
    "data" : [
        "views/estudiantes_views.xml",
        "views/res_company.xml",
        "views/estados_views.xml",
        "views/municipios_views.xml",
        "views/parroquias_views.xml",
        "views/deportes_views.xml",
        "views/familiares_contactos_views.xml",
        "views/reporte_estudiante.xml",
        "reportes/estudiante_unefa.xml",
        ],
    'installable': True,
    'auto_install': False,
}
