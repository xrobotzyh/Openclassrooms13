from django.db import migrations


def migrate_datas(apps, schema_editor):
    """

    """
    old_address = apps.get_model('oc_lettings_site', 'Address')
    old_letting = apps.get_model('oc_lettings_site', 'Letting')
    old_profile = apps.get_model('oc_lettings_site', 'Profile')

    new_address = apps.get_model('lettings', 'Address')
    new_address.objects.bulk_create(
        new_address(number=old_object.number, street=old_object.street, city=old_object.city, state=old_object.state,
                    zip_code=old_object.zip_code, country_iso_code=old_object.country_iso_code)
        for old_object in old_address.objects.all()
    )

    new_letting = apps.get_model('lettings', 'Letting')
    new_letting.objects.bulk_create(
        new_letting(title=old_object.title, address_id=old_object.address_id)
        for old_object in old_letting.objects.all()
    )

    new_profile = apps.get_model('profiles', 'Profile')
    new_profile.objects.bulk_create(
        new_profile(favorite_city=old_object.favorite_city, user_id=old_object.user_id)
        for old_object in old_profile.objects.all()
    )


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_datas),
    ]
