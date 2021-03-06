from datetime import datetime
from django.core.management.base import BaseCommand, CommandError

from qp.world.models import qpWorld
from qp.forum.models import (
    qpForum,
    qpForumZone,
    qpForumTerritory,
    qpForumSector
)

class Command(BaseCommand):
    help = "initialize the world and forum Rhansidor"

    # def add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start initializing................"))

        try:
            world, created = qpWorld.objects.get_or_create(
                name=str("Rhansidor"),
                slug=str("rhansidor"),
                visibility=0
            )
            world.created_at = datetime(2015, 1, 1, 0, 0, 0)
            world.save()
            self.stdout.write("World : %s" % str(world.name))
            forum, created = qpForum.objects.get_or_create(
                world=world,
                name=str("Rhansidor"),
                visibility=0
            )
            self.stdout.write("Forum : %s" % str(forum.name))
            self.init_dolgaran(forum)

        except Exception as e:
            raise CommandError("An error occurred : ", e)

        self.stdout.write(self.style.SUCCESS("................. end initializing"))
    
    def init_dolgaran(self, forum):
        self.stdout.write(self.style.WARNING(">> Start init Dolgaran ..."))
        zone, created = qpForumZone.objects.get_or_create(
            forum=forum,
            name=str("Dolgaran, le continent")
        )
        self.stdout.write("Zone : %s" % str(zone.name))
        self.init_ingvar(zone)
        self.init_briareus(zone)
        self.init_nelryn(zone)
        self.init_herior(zone)
        self.init_azzam(zone)
        self.init_seldszar(zone)
        self.stdout.write(self.style.WARNING("... end init Dolgaran <<"))
    
    def init_ingvar(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Ingvar ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Ingvar, la terre gel??e"),
            description=str("Les contr??es du nord sont les plus froides de tout Rhansidor. Ces terres sauvages et glaciales abritent bon nombre de cr??atures mais les Terkhel qui y vivent sont aussi redoutables et t??m??raires que la faune hostile de leur pays."),
            colour="#3f197c",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Toundra d'Arghansdir"),
            description=str("Cette zone repr??sente la grande majorit?? d'Ingvar. Pour ceux qui ne sont pas de ces terres, la Toundra est un lieu particuli??rement dangereux, d'autant qu'il fascine par la beaut?? de ses d??cors enneig??s."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("La cha??ne de Vemund"),
            description=str("Elle longe tout le c??t?? ouest du pays et abrite le clan constitu?? uniquement de femmes. C'est parce que cet endroit est le plus froid et dur du pays qu'elles s'y sont install??es, marquant ainsi leur domination et offrant ?? leurs rivaux une barri??re naturelle pour les emp??cher de les atteindre."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Brume-Claire"),
            description=str("Un lac immense plac?? en plein milieu des terres gel??es, il porte son nom de la brume qui s'??chappe de la glace et peut tr??s vite rendre la vision difficile pour quiconque contourne le lac ou vogue dessus."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Sitvaar"),
            description=str("La citadelle noire fut construite par les noir-sang et occup??e par ceux-ci durant des si??cles. A pr??sent que le clan est dissout, Sitvaar sert de capitale ?? Ingvar. Notamment connue pour son ar??ne, ?? pr??sent ce sont des hommes libres qui y combattent pour le plaisir face ?? d'autres combattants ou de dangereuses cr??atures peuplant Rhansidor."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Ingvar <<"))
    
    def init_briareus(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Briareus ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Briareus, la sauvage"),
            description=str("Ces terres immenses n'appartiennent ?? personne et font l'objet de la fascination de tous pour ses d??cors invraisemblables qui abritent ??norm??ment de dangers et de secrets."),
            colour="#744f1a",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("So??mhur"),
            description=str("Une ??tendue jonch??e de cristaux de rhandolytes. Fut un temps o?? cet endroit aurait ??t?? la source de conflits, mais ?? pr??sent ce n'est qu'un lieu parmi tant d'autres."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("La jungle de Vrynh"),
            description=str("Cette zone est grande et cache un nombre incalculable de cr??atures. On y croise aussi beaucoup de groupes d'Oonkha?? car cette zone est un terrain de chasse."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Balvhor, chemin des sages"),
            description=str("Cet endroit est le passage principal des voyageurs qui cherchent ?? traverser Briareus. Elle ne poss??de qu???une seule route bord??e par d'anciennes reliques de technologie qui ??clairent l'endroit d'un flux de rad??ons sur votre passage."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Ho'kee"),
            description=str("Ruines d'une ancienne civilisation, Ho'kee se trouve entre Nelryn et Azzam, lov?? dans les falaises de Briareus juste en bordure de l'oc??an. C'est dans ce petit village que logent les O'zewah qui cohabitent avec des Pachu'a, formant ainsi une communaut?? soud??e et prot??g??e des pr??dateurs."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Briareus <<"))
    
    def init_nelryn(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Nelryn ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Nelryn, le littoral"),
            description=str("Une des zones o?? il fait bon vivre. Le littoral y accueille la tribu des O'ahus. Ici, la mer est au c??ur de tout... Malheureusement, malgr?? la beaut?? de l'endroit, cette zone est tout aussi dangereuse que d'autres. Oc??an capricieux, monstres colossaux..."),
            colour="#197173",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Onholua"),
            description=str("La cit?? du littoral inspire au calme et ?? la paix. Ici, beaucoup de commerce se fait avec les autres tribus, tout tourne autour de la p??che, la m??decine et la navigation."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Le lagon Ihuel"),
            description=str("Un endroit propice ?? la p??che. La barri??re de corail du lagon regorge de cr??atures marines et de plantes aquatiques tr??s pris??es par la tribu du coin."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Les grottes cach??es d'Awulah"),
            description=str("Quelque part dans le littoral se trouve un r??seau de grottes paisibles. Beaucoup de rituels y sont r??alis??s par la tribu du coin pour leur d??it??. Hormis cela, les gens y viennent aussi pour p??cher et ramasser ce que la mer rejette dans les grottes."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Melo'wee, les Milles Cascades"),
            description=str("Les arbres sont ici ?? ce point enchev??tr??s que leurs branches forment de larges bassins v??g??taux suspendus qui retiennent l'eau de pluie ?? diverses hauteurs. Elle s'??coule parfois en myriade de petites cascades, nappant d'eau les terrasses naturelles et rocheuses du sol avant de plonger dans le lagon."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Nelryn <<"))
    
    def init_herior(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Herior ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Herior, la sylve"),
            description=str("Herior n'est pas un pays, c'est une gigantesque for??t qui s?????tend sur des milliers de kilom??tres. Consid??r??e comme sacr??e par la tribu qui l???habite, cet endroit est le berceau de la vie et de la sagesse au sein de Rhansidor."),
            colour="#1f7419",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Isa??n"),
            description=str("Cit?? unique du peuple de la for??t, c'est ici que sont regroup??s tous ses habitants. Il existe un chemin qui traverse toute la zone pour s'y rendre, tr??s facile d'acc??s mais pas d??nu?? de dangers, m??fiance donc."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Le marais d'Ysenmor"),
            description=str("Croyez-le, ici vous ne voudrez pas y poser les pieds. L'endroit est lugubre et naus??abond mais il s'av??re que c'est aussi un parfait endroit o?? chasser. Peut-??tre survivrez-vous assez longtemps pour revenir avec votre gibier..."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Elur"),
            description=str("Dit la clairi??re aux champignons. Car ici, pas un seul arbre mais juste des champignons de toutes sortes, de toutes couleurs mais surtout d'une taille ??norme. Attention, ce lieu abrite n??anmoins bon nombre de cr??atures, prenez garde."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Xe??a"),
            description=str("Xe??a est un petit bosquet au nord d'Herior o?? de larges troncs, d??vast??s par le pr??c??dent cataclysme, pr??servent d'importantes sources de Rhandolyte. Ces lieux abritent ??galement un petit observatoire o?? des ??rudits ??tudient l'astronomie. La luminescence permet ?? quiconque s'y aventurant de se rep??rer parmi les arbres noircis par le temps..."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Herior <<"))
    
    def init_azzam(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Azz??m ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Azz??m, l'ardent"),
            description=str("Comme son nom le laisse comprendre, ce d??sert de sable est d'une chaleur presque ??touffante. Le peuple qui vit ici s'est habitu?? il y des si??cles de cela ?? vivre dans des conditions extr??mes. Cette zone dangereuse n'est pas ?? prendre ?? la l??g??re."),
            colour="#78750c",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Haykal"),
            description=str("La somptueuse cit?? de la tribu du d??sert est un v??ritable joyau architectural envi?? par bon nombre de peuples. Bien qu'elle soit dans le d??sert, celle-ci fut construite au bord de l'eau, apportant ainsi tout le n??cessaire ?? la survie de son peuple."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Le canyon"),
            description=str("Comme son nom l'indique... C'est un canyon, un amas de montagnes d??sertiques o?? r??gne une chaleur aussi forte que dans le reste du d??sert. Cette zone poss??de un r??seau de mines dans lequel la tribu du coin r??colte tout le n??cessaire pour la richesse de celui-ci."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Les ruines mouvantes"),
            description=str("D'antiques habitations en ruine, tour ?? tour recouvertes puis d??couvertes par le sable : il est pr??f??rable de ne pas y dormir, sauf si go??t prononc?? pour les petits-d??jeuners craquants. Les l??gendes ??voquent une cit?? souterraine, mais seuls les fous revenant les mains vides semblent en avoir d??couvert des acc??s au sein des ruines."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Baie de Mansoor"),
            description=str("Situ??e entre Nelryn et Haykal, les navires marchands y font halte. Etendue de plages tropicales, la baie est connue pour ses comptoirs commerciaux, ses lieux de plaisir, et ses auberges aux mille transactions. Plus loin dans les terres on y trouve des monuments sculpt??s ?? m??me la roche, endroit id??al pour les f??rus d'exploration."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Azz??m <<"))
    
    def init_seldszar(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Seldszar ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Seldszar, la sombre"),
            description=str("Rien ici ne pourra vous inspirer l'envie de vous y aventurer. C'est la zone la plus infecte de tout Rhansidor, se trouvant en plein c??ur du continent. Berceau de l'arme qui autrefois causa le cataclysme, c'est aujourd'hui une terre d??sol??e o?? vivent les sanguinaires."),
            colour="#742419",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Yazston"),
            description=str("Au c??ur de Seldszar se trouve ce village immonde o?? logent les sanguinaires. Immense et construit de fa??on basique et d??sordonn??e, il entoure le radian principal qui fut ?? l'origine du cataclysme."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Les landes mortes"),
            description=str("Cette terre accueille rarement la lumi??re et la seule chose que l'on trouve ?? cet endroit c'est le silence et la mort... qui vous sera sans doute donn??e par les cr??atures des environs ou bien les sanguinaires eux-m??mes."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Seldszar <<"))