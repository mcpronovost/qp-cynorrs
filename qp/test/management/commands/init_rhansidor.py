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
                name=str("Rhansidor")
            )
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
            name=str("Ingvar, la terre gelée"),
            description=str("Les contrées du nord sont les plus froides de tout Rhansidor. Ces terres sauvages et glaciales abritent bon nombre de créatures mais les Terkhel qui y vivent sont aussi redoutables et téméraires que la faune hostile de leur pays."),
            colour="#3f197c",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Toundra d'Arghansdir"),
            description=str("Cette zone représente la grande majorité d'Ingvar. Pour ceux qui ne sont pas de ces terres, la Toundra est un lieu particulièrement dangereux, d'autant qu'il fascine par la beauté de ses décors enneigés."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("La chaîne de Vemund"),
            description=str("Elle longe tout le côté ouest du pays et abrite le clan constitué uniquement de femmes. C'est parce que cet endroit est le plus froid et dur du pays qu'elles s'y sont installées, marquant ainsi leur domination et offrant à leurs rivaux une barrière naturelle pour les empêcher de les atteindre."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Brume-Claire"),
            description=str("Un lac immense placé en plein milieu des terres gelées, il porte son nom de la brume qui s'échappe de la glace et peut très vite rendre la vision difficile pour quiconque contourne le lac ou vogue dessus."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Sitvaar"),
            description=str("La citadelle noire fut construite par les noir-sang et occupée par ceux-ci durant des siècles. A présent que le clan est dissout, Sitvaar sert de capitale à Ingvar. Notamment connue pour son arène, à présent ce sont des hommes libres qui y combattent pour le plaisir face à d'autres combattants ou de dangereuses créatures peuplant Rhansidor."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Ingvar <<"))
    
    def init_briareus(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Briareus ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Briareus, la sauvage"),
            description=str("Ces terres immenses n'appartiennent à personne et font l'objet de la fascination de tous pour ses décors invraisemblables qui abritent énormément de dangers et de secrets."),
            colour="#744f1a",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Soömhur"),
            description=str("Une étendue jonchée de cristaux de rhandolytes. Fut un temps où cet endroit aurait été la source de conflits, mais à présent ce n'est qu'un lieu parmi tant d'autres."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("La jungle de Vrynh"),
            description=str("Cette zone est grande et cache un nombre incalculable de créatures. On y croise aussi beaucoup de groupes d'Oonkhaï car cette zone est un terrain de chasse."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Balvhor, chemin des sages"),
            description=str("Cet endroit est le passage principal des voyageurs qui cherchent à traverser Briareus. Elle ne possède qu’une seule route bordée par d'anciennes reliques de technologie qui éclairent l'endroit d'un flux de radéons sur votre passage."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Ho'kee"),
            description=str("Ruines d'une ancienne civilisation, Ho'kee se trouve entre Nelryn et Azzam, lové dans les falaises de Briareus juste en bordure de l'océan. C'est dans ce petit village que logent les O'zewah qui cohabitent avec des Pachu'a, formant ainsi une communauté soudée et protégée des prédateurs."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Briareus <<"))
    
    def init_nelryn(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Nelryn ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Nelryn, le littoral"),
            description=str("Une des zones où il fait bon vivre. Le littoral y accueille la tribu des O'ahus. Ici, la mer est au cœur de tout... Malheureusement, malgré la beauté de l'endroit, cette zone est tout aussi dangereuse que d'autres. Océan capricieux, monstres colossaux..."),
            colour="#197173",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Onholua"),
            description=str("La cité du littoral inspire au calme et à la paix. Ici, beaucoup de commerce se fait avec les autres tribus, tout tourne autour de la pêche, la médecine et la navigation."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Le lagon Ihuel"),
            description=str("Un endroit propice à la pêche. La barrière de corail du lagon regorge de créatures marines et de plantes aquatiques très prisées par la tribu du coin."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Les grottes cachées d'Awulah"),
            description=str("Quelque part dans le littoral se trouve un réseau de grottes paisibles. Beaucoup de rituels y sont réalisés par la tribu du coin pour leur déité. Hormis cela, les gens y viennent aussi pour pêcher et ramasser ce que la mer rejette dans les grottes."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Melo'wee, les Milles Cascades"),
            description=str("Les arbres sont ici à ce point enchevêtrés que leurs branches forment de larges bassins végétaux suspendus qui retiennent l'eau de pluie à diverses hauteurs. Elle s'écoule parfois en myriade de petites cascades, nappant d'eau les terrasses naturelles et rocheuses du sol avant de plonger dans le lagon."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Nelryn <<"))
    
    def init_herior(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Herior ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Herior, la sylve"),
            description=str("Herior n'est pas un pays, c'est une gigantesque forêt qui s’étend sur des milliers de kilomètres. Considérée comme sacrée par la tribu qui l’habite, cet endroit est le berceau de la vie et de la sagesse au sein de Rhansidor."),
            colour="#1f7419",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Isaën"),
            description=str("Cité unique du peuple de la forêt, c'est ici que sont regroupés tous ses habitants. Il existe un chemin qui traverse toute la zone pour s'y rendre, très facile d'accès mais pas dénué de dangers, méfiance donc."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Le marais d'Ysenmor"),
            description=str("Croyez-le, ici vous ne voudrez pas y poser les pieds. L'endroit est lugubre et nauséabond mais il s'avère que c'est aussi un parfait endroit où chasser. Peut-être survivrez-vous assez longtemps pour revenir avec votre gibier..."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Elur"),
            description=str("Dit la clairière aux champignons. Car ici, pas un seul arbre mais juste des champignons de toutes sortes, de toutes couleurs mais surtout d'une taille énorme. Attention, ce lieu abrite néanmoins bon nombre de créatures, prenez garde."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Xeïa"),
            description=str("Xeïa est un petit bosquet au nord d'Herior où de larges troncs, dévastés par le précédent cataclysme, préservent d'importantes sources de Rhandolyte. Ces lieux abritent également un petit observatoire où des érudits étudient l'astronomie. La luminescence permet à quiconque s'y aventurant de se repérer parmi les arbres noircis par le temps..."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Herior <<"))
    
    def init_azzam(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Azzàm ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Azzàm, l'ardent"),
            description=str("Comme son nom le laisse comprendre, ce désert de sable est d'une chaleur presque étouffante. Le peuple qui vit ici s'est habitué il y des siècles de cela à vivre dans des conditions extrêmes. Cette zone dangereuse n'est pas à prendre à la légère."),
            colour="#78750c",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Haykal"),
            description=str("La somptueuse cité de la tribu du désert est un véritable joyau architectural envié par bon nombre de peuples. Bien qu'elle soit dans le désert, celle-ci fut construite au bord de l'eau, apportant ainsi tout le nécessaire à la survie de son peuple."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Le canyon"),
            description=str("Comme son nom l'indique... C'est un canyon, un amas de montagnes désertiques où règne une chaleur aussi forte que dans le reste du désert. Cette zone possède un réseau de mines dans lequel la tribu du coin récolte tout le nécessaire pour la richesse de celui-ci."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Les ruines mouvantes"),
            description=str("D'antiques habitations en ruine, tour à tour recouvertes puis découvertes par le sable : il est préférable de ne pas y dormir, sauf si goût prononcé pour les petits-déjeuners craquants. Les légendes évoquent une cité souterraine, mais seuls les fous revenant les mains vides semblent en avoir découvert des accès au sein des ruines."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Baie de Mansoor"),
            description=str("Située entre Nelryn et Haykal, les navires marchands y font halte. Etendue de plages tropicales, la baie est connue pour ses comptoirs commerciaux, ses lieux de plaisir, et ses auberges aux mille transactions. Plus loin dans les terres on y trouve des monuments sculptés à même la roche, endroit idéal pour les férus d'exploration."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Azzàm <<"))
    
    def init_seldszar(self, zone):
        self.stdout.write(self.style.NOTICE(">> Start init Seldszar ..."))
        territory, created = qpForumTerritory.objects.get_or_create(
            zone=zone,
            name=str("Seldszar, la sombre"),
            description=str("Rien ici ne pourra vous inspirer l'envie de vous y aventurer. C'est la zone la plus infecte de tout Rhansidor, se trouvant en plein cœur du continent. Berceau de l'arme qui autrefois causa le cataclysme, c'est aujourd'hui une terre désolée où vivent les sanguinaires."),
            colour="#742419",
            flexbasis="33.3333%"
        )
        self.stdout.write("Territory : %s" % str(territory.name))
        # ===--- sectors
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Yazston"),
            description=str("Au cœur de Seldszar se trouve ce village immonde où logent les sanguinaires. Immense et construit de façon basique et désordonnée, il entoure le radian principal qui fut à l'origine du cataclysme."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        sector, created = qpForumSector.objects.get_or_create(
            territory=territory,
            name=str("Les landes mortes"),
            description=str("Cette terre accueille rarement la lumière et la seule chose que l'on trouve à cet endroit c'est le silence et la mort... qui vous sera sans doute donnée par les créatures des environs ou bien les sanguinaires eux-mêmes."),
            flexbasis="50%"
        )
        self.stdout.write("Sector : %s" % str(sector.name))
        self.stdout.write(self.style.NOTICE("... end init Seldszar <<"))