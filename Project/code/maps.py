#This file contains map information.

import networkx as nx

#Initialize map graphs
coastline = nx.DiGraph()
border = nx.DiGraph()
kafedostoyevsky = nx.DiGraph()
clubhouse = nx.DiGraph()
villa = nx.DiGraph()
consulate = nx.DiGraph()
bank = nx.DiGraph()

#Define map spawns
coastline_atk_spawns = ['EXTMAINENTRANCE', 'EXTPOOLSIDE', 'EXTRUINS']
coastline_def_spawns = ['2FPENTHOUSE', '2FTHEATER', '2FBILLIARDSROOM', '2FHOOKAHLOUNGE', '1FSERVICEENTRANCE', '1FKITCHEN', '1FBLUEBAR', '1FSUNRISEBAR']
border_atk_spawns = ['EXTVALLEY', 'EXTWESTVEHEXIT', 'EXTEASTVEHENT']
border_def_spawns = ['1FSERVERROOM', '2FARMORYLOCKERS', '1FCUSTOMSINSPECTION', '1FTELLERS']
kafedostoyevsky_atk_spawns = ['EXTRIVERDOCKS', 'EXTCHRISTMASMARKET', 'EXTPARK']
kafedostoyevsky_def_spawns = ['3FBAR', '1FKITCHENCOOKING', '1FKITCHENSERVICE', '2FREADINGROOMCORRIDOR', '2FREADINGROOM', '2FFIREPLACEHALL', '2FTRAINMUSEUM', '2FMININGROOM']
clubhouse_atk_spawns = ['EXTCONSTRUCTIONSITE', 'EXTWAREHOUSE', 'EXTSHIPPINGDOCK', 'EXTMAINGATE']
clubhouse_def_spawns = ['BCHURCH', '2FCASHROOM', '2FBEDROOM', '1FSTAGE']
villa_atk_spawns = []
villa_def_spawns = []
consulate_atk_spawns = []
consulate_def_spawns = []
bank_atk_spawns = []
bank_def_spawns = []
#Define dictionary to store map spawns. Index 0 is atk and index 1 is def.
map_spawns = {
    'COASTLINE':{'ATK':coastline_atk_spawns, 'DEF':coastline_def_spawns},
    'BORDER':{'ATK':border_atk_spawns, 'DEF':border_def_spawns},
    'KAFEDOSTOYEVSKY':{'ATK':kafedostoyevsky_atk_spawns, 'DEF':kafedostoyevsky_def_spawns},
    'CLUBHOUSE':{'ATK':clubhouse_atk_spawns, 'DEF':clubhouse_def_spawns},
    'VILLA':{'ATK':villa_atk_spawns, 'DEF':villa_def_spawns},
    'CONSULATE':{'ATK':consulate_atk_spawns, 'DEF':consulate_def_spawns},
    'BANK':{'ATK':bank_atk_spawns, 'DEF':bank_def_spawns}
}

#Define map_strings list
map_strings = list(map_spawns.keys())

#Add default open rooms for each map
#Note doors and windows that can be barricaded count as open
coastline.add_edges_from([
    ('EXTMAINENTRANCE', 'EXTPOOL'), ('EXTMAINENTRANCE', 'EXTBACKALLEY'), ('EXTMAINENTRANCE', 'EXTGARAGEROOF'), ('EXTMAINENTRANCE', 'EXTSOUTHPROMENADE'), ('EXTMAINENTRANCE', 'EXTROOFTOP'), ('EXTMAINENTRANCE', '2FHALLWAY'), ('EXTMAINENTRANCE', '1FSERVICEENTRANCE'), ('EXTMAINENTRANCE', '2FPENTHOUSE'), ('EXTMAINENTRANCE', '1FMAINLOBBY'), ('EXTMAINENTRANCE', 'EXTDJBOOTH'),
    ('EXTGARAGEROOF', 'EXTBACKALLEY'), ('EXTGARAGEROOF', 'EXTPOOL'), ('EXTGARAGEROOF', 'EXTMAINENTRANCE'),
    ('EXTBACKALLEY', 'EXTGARAGEROOF'), ('EXTBACKALLEY', 'EXTPOOL'), ('EXTBACKALLEY', 'EXTMAINENTRANCE'), ('EXTBACKALLEY', 'EXTPOOLSIDE'),
    ('EXTPOOL', 'EXTMAINENTRANCE'), ('EXTPOOL', 'EXTGARAGEROOF'), ('EXTPOOL', 'EXTBACKALLEY'), ('EXTPOOL', 'EXTDJBOOTH'), ('EXTPOOL', 'EXTCANTINA'), ('EXTPOOL', 'EXTPOOLSIDE'), ('EXTPOOL', 'EXTROOFTOP'), ('EXTPOOL', '2FHOOKAHLOUNGE'), ('EXTPOOL', '1FPOOLENTRANCE'), ('EXTPOOL', 'EXTRUINS'), ('EXTPOOL', 'EXTHOOKAHDECK'), ('EXTPOOL', 'EXTWALKWAY'),
    ('EXTPOOLSIDE', 'EXTBACKALLEY'), ('EXTPOOLSIDE', 'EXTPOOL'), ('EXTPOOLSIDE', 'EXTWALKWAY'),
    ('EXTWALKWAY', 'EXTPOOLSIDE'), ('EXTWALKWAY', 'EXTPOOL'), ('EXTWALKWAY', 'EXTRUINS'),
    ('EXTCANTINA', 'EXTPOOL'), ('EXTCANTINA', '1FKITCHEN'),
    ('EXTRUINS', 'EXTPOOL'), ('EXTRUINS', 'EXTWALKWAY'), ('EXTRUINS', '1FPOOLENTRANCE'), ('EXTRUINS', 'EXTHOOKAHDECK'), ('EXTRUINS', '1FSUNRISEBAR'), ('EXTRUINS', 'EXTROOFTOP'), ('EXTRUINS', '1FBLUEBAR'), ('EXTRUINS', '2FBILLIARDSROOM'), ('EXTRUINS', 'EXTTERRACE'), ('EXTRUINS', 'EXTSOUTHPROMENADE'), ('EXTRUINS', 'EXTBALCONY'),
    ('EXTTERRACE', 'EXTBALCONY'), ('EXTTERRACE', 'EXTRUINS'), ('EXTTERRACE', 'EXTSOUTHPROMENADE'), ('EXTTERRACE','1FOFFICE'),
    ('EXTSOUTHPROMENADE', 'EXTRUINS'), ('EXTSOUTHPROMENADE', 'EXTTERRACE'), ('EXTSOUTHPROMENADE', 'EXTROOFTOP'), ('EXTSOUTHPROMENADE', '1FSUNROOM'), ('EXTSOUTHPROMENADE', '2FSOUTHHALLYWAY'), ('EXTSOUTHPROMENADE', 'EXTMAINENTRANCE'), ('EXTSOUTHPROMENADE', 'EXTBALCONY'), ('EXTSOUTHPROMENADE', '1FSECURITYROOM'),
    ('EXTBALCONY', 'EXTTERRACE'), ('EXTBALCONY', 'EXTROOFTOP'), ('EXTBALCONY', 'EXTRUINS'), ('EXTBALCONY', 'EXTSOUTHPROMENADE'), ('EXTBALCONY', '2FAQUARIUM'),
    ('EXTHOOKAHDECK', 'EXTROOFTOP'), ('EXTHOOKAHDECK', 'EXTRUINS'), ('EXTHOOKAHDECK', 'EXTPOOL'), ('EXTHOOKAHDECK', '2FHOOKAHLOUNGE'),
    ('EXTDJBOOTH', '2FHALLOFFAME'), ('EXTDJBOOTH', 'EXTPOOL'), ('EXTDJBOOTH', 'EXTMAINENTRANCE'), ('EXTDJBOOTH', '2FVIPLOUNGE'),
    ('EXTROOFTOP', 'EXTHOOKAHDECK'), ('EXTROOFTOP', 'EXTPOOL'), ('EXTROOFTOP', 'EXTSOUTHPROMENADE'), ('EXTROOFTOP', 'EXTMAINENTRANCE'), ('EXTROOFTOP', 'EXTBALCONY'), ('EXTROOFTOP', 'EXTRUINS'), ('EXTROOFTOP', '1FCOURTYARD'),
    ('1FCOURTYARD', 'EXTROOFTOP'), ('1FCOURTYARD', '1FMAINLOBBY'), ('1FCOURTYARD', '1FHALLWAY'), ('1FCOURTYARD', '2FHALLWAY'), ('1FCOURTYARD', '2FSOUTHHALLYWAY'),
    ('1FMAINLOBBY', '1FCOURTYARD'), ('1FMAINLOBBY', '1FTOILETS'), ('1FMAINLOBBY', '1FHALLWAY'), ('1FMAINLOBBY', 'EXTMAINENTRANCE'), ('1FMAINLOBBY', '1FSECURITYROOM'), ('1FMAINLOBBY', '2FHALLWAY'),
    ('1FTOILETS', '1FMAINLOBBY'), ('1FTOILETS', '1FSERVICEENTRANCE'),
    ('1FSERVICEENTRANCE', 'EXTMAINENTRANCE'), ('1FSERVICEENTRANCE', '1FTOILETS'), ('1FSERVICEENTRANCE', '1FKITCHEN'),
    ('1FKITCHEN', '1FSERVICEENTRANCE'), ('1FKITCHEN', 'EXTCANTINA'), ('1FKITCHEN', '1FHALLWAY'),
    ('1FHALLWAY', '1FKITCHEN'), ('1FHALLWAY', '1FMAINLOBBY'), ('1FHALLWAY', '1FCOURTYARD'), ('1FHALLWAY', '1FSUNRISEBAR'), ('1FHALLWAY', '1FBLUEBAR'), ('1FHALLWAY', '1FNORTHSTAIRS'),
    ('1FNORTHSTAIRS', '1FHALLWAY'), ('1FNORTHSTAIRS', '2FHALLWAY'),
    ('1FSUNRISEBAR', '1FHALLWAY'), ('1FSUNRISEBAR', '1FPOOLENTRANCE'), ('1FSUNRISEBAR', 'EXTRUINS'),
    ('1FBLUEBAR', '1FOFFICE'), ('1FBLUEBAR', '1FHALLWAY'), ('1FBLUEBAR', 'EXTRUINS'),
    ('2FHALLWAY', '1FNORTHSTAIRS'), ('2FHALLWAY', '2FHOOKAHLOUNGE'), ('2FHALLWAY', '2FBILLIARDSROOM'), ('2FHALLWAY', '1FCOURTYARD'), ('2FHALLWAY', '2FVIPLOUNGE'), ('2FHALLWAY', '2FTHEATER'), ('2FHALLWAY', '1FMAINLOBBY'), ('2FHALLWAY', '2FSOUTHHALLYWAY'), ('2FHALLWAY', 'EXTMAINENTRANCE'),
    ('2FHOOKAHLOUNGE', 'EXTHOOKAHDECK'), ('2FHOOKAHLOUNGE', 'EXTPOOL'), ('2FHOOKAHLOUNGE', '2FHALLWAY'),
    ('2FBILLIARDSROOM', '2FHALLWAY'), ('2FBILLIARDSROOM', '2FAQUARIUM'), ('2FBILLIARDSROOM', 'EXTRUINS'),
    ('2FAQUARIUM', '2FBILLIARDSROOM'), ('2FAQUARIUM', 'EXTBALCONY'), ('2FAQUARIUM', '2FSOUTHHALLYWAY'),
    ('2FSOUTHHALLYWAY', '2FAQUARIUM'), ('2FSOUTHHALLYWAY', '2FHALLWAY'), ('2FSOUTHHALLYWAY', '1FCOURTYARD'), ('2FSOUTHHALLYWAY', 'EXTSOUTHPROMENADE'),
    ('2FVIPLOUNGE', '2FHALLWAY'), ('2FVIPLOUNGE', '2FHALLOFFAME'), ('2FVIPLOUNGE', 'EXTDJBOOTH'),
    ('2FHALLOFFAME', '2FVIPLOUNGE'), ('2FHALLOFFAME', '2FPENTHOUSE'), ('2FHALLOFFAME', 'EXTDJBOOTH'),
    ('2FPENTHOUSE', '2FBATHROOM'), ('2FPENTHOUSE', '2FHALLOFFAME'), ('2FPENTHOUSE', '2FTHEATER'), ('2FPENTHOUSE', 'EXTMAINENTRANCE'),
    ('2FTHEATER', '2FPENTHOUSE'), ('2FTHEATER', '2FHALLWAY'),
    ('1FSECURITYROOM', 'EXTSOUTHPROMENADE'), ('1FSECURITYROOM', '1FMAINLOBBY'), ('1FSECURITYROOM', '1FSUNROOM'),
    ('1FSUNROOM', '1FOFFICE'), ('1FSUNROOM', '1FSECURITYROOM'), ('1FSUNROOM', 'EXTSOUTHPROMENADE'),
    ('1FOFFICE', 'EXTTERRACE'), ('1FOFFICE', '1FSUNROOM'), ('1FOFFICE', '1FBLUEBAR'),
    ('1FPOOLENTRANCE', '1FSUNRISEBAR'), ('1FPOOLENTRANCE', 'EXTRUINS'), ('1FPOOLENTRANCE', 'EXTPOOL'),
    ('2FBATHROOM', '2FPENTHOUSE')
], open = True, edge_visited_ATK = 0, edge_visited_DEF = 0, deaths_ATK = 0, deaths_DEF = 0)

#There are some ghost edges that will always be 0 but exist for the testing:
#('1FWAITINGROOM', 'EXTSOUTHBALCONY')
#('1FWAITINGROOM', '2FMAINHALLWAY')
border.add_edges_from([
    ('EXTVALLEY', 'EXTPARKINGLOTENT'), ('EXTVALLEY', 'EXTPEDESTRIANCUSTOMS'), ('EXTVALLEY', 'EXTWATCHTOWER'),
    ('EXTWATCHTOWER', 'EXTVALLEY'), ('EXTWATCHTOWER', 'EXTPEDESTRIANCUSTOMS'),
    ('EXTPEDESTRIANCUSTOMS', 'EXTVALLEY'), ('EXTPEDESTRIANCUSTOMS', 'EXTWATCHTOWER'), ('EXTPEDESTRIANCUSTOMS', 'EXTSOUTHBALCONY'), ('EXTPEDESTRIANCUSTOMS', 'EXTPARKINGLOTENT'), ('EXTPEDESTRIANCUSTOMS', 'EXTROOF'), ('EXTPEDESTRIANCUSTOMS', 'EXTEASTALLEY'), ('EXTPEDESTRIANCUSTOMS', 'EXTPEDESTRIANENTRANCE'), ('EXTPEDESTRIANCUSTOMS', '1FPASSPORTCHECK'),
    ('EXTPARKINGLOTENT', 'EXTPEDESTRIANCUSTOMS'), ('EXTPARKINGLOTENT', 'EXTVALLEY'), ('EXTPARKINGLOTENT', 'EXTPEDESTRIANEXIT'), ('EXTPARKINGLOTENT', 'EXTPARKINGLOT'), ('EXTPARKINGLOTENT', 'EXTPARKINGLOTALLEY'), ('EXTPARKINGLOTENT', 'EXTWESTBALCONY'), ('EXTPARKINGLOTENT', 'EXTROOF'),
    ('EXTPEDESTRIANEXIT', 'EXTPARKINGLOTENT'), ('EXTPEDESTRIANEXIT', 'EXTWESTTOWER'), ('EXTPEDESTRIANEXIT', 'EXTWESTVEHEXIT'),
    ('EXTWESTVEHEXIT', 'EXTPEDESTRIANEXIT'), ('EXTWESTVEHEXIT', 'EXTWESTTOWER'), ('EXTWESTVEHEXIT', 'EXTWESTROAD'),
    ('EXTWESTTOWER', 'EXTPEDESTRIANEXIT'), ('EXTWESTTOWER', 'EXTWESTVEHEXIT'), ('EXTWESTTOWER', 'EXTWESTROAD'), ('EXTWESTTOWER', 'EXTPARKINGLOT'),
    ('EXTWESTROAD', 'EXTWESTVEHEXIT'), ('EXTWESTROAD', 'EXTWESTTOWER'), ('EXTWESTROAD', 'EXTPARKINGLOT'), ('EXTWESTROAD', 'EXTVEHICLECUSTOMS'), ('EXTWESTROAD', 'EXTPARKINGLOTALLEY'),
    ('EXTPARKINGLOT', 'EXTWESTROAD'), ('EXTPARKINGLOT', 'EXTWESTTOWER'), ('EXTPARKINGLOT', 'EXTPARKINGLOTALLEY'), ('EXTPARKINGLOT', 'EXTPARKINGLOTENT'),
    ('EXTPARKINGLOTALLEY', 'EXTPARKINGLOT'), ('EXTPARKINGLOTALLEY', 'EXTPARKINGLOTENT'), ('EXTPARKINGLOTALLEY', 'EXTWESTROAD'), ('EXTPARKINGLOTALLEY', 'EXTVEHICLECUSTOMS'), ('EXTPARKINGLOTALLEY', 'EXTROOF'), ('EXTPARKINGLOTALLEY', 'EXTWESTBALCONY'), ('EXTPARKINGLOTALLEY', '1FEXITHALLWAY'), ('EXTPARKINGLOTALLEY', '1FSUPPLYROOM'),
    ('EXTVEHICLECUSTOMS', 'EXTROOF'), ('EXTVEHICLECUSTOMS', 'EXTPARKINGLOTALLEY'), ('EXTVEHICLECUSTOMS', 'EXTWESTROAD'), ('EXTVEHICLECUSTOMS', '1FVENTILATIONROOM'), ('EXTVEHICLECUSTOMS', '2FARMORYLOCKERS'), ('EXTVEHICLECUSTOMS', '2FARCHIVES'), ('EXTVEHICLECUSTOMS', 'EXTCRASHSCENE'),
    ('EXTCRASHSCENE', 'EXTVEHICLECUSTOMS'), ('EXTCRASHSCENE', 'EXTROOF'), ('EXTCRASHSCENE', 'EXTNORTHBALCONY'), ('EXTCRASHSCENE', 'EXTEASTALLEY'), ('EXTCRASHSCENE', 'EXTEASTBALCONY'), ('EXTCRASHSCENE', 'EXTEASTROAD'),
    ('EXTEASTROAD', 'EXTEASTVEHENT'), ('EXTEASTROAD', 'EXTCRASHSCENE'), ('EXTEASTROAD', 'EXTEASTALLEY'),
    ('EXTEASTVEHENT', 'EXTEASTROAD'), ('EXTEASTVEHENT', 'EXTPEDESTRIANENTRANCE'),
    ('EXTEASTALLEY', '1FTELLERS'), ('EXTEASTALLEY', 'EXTROOF'), ('EXTEASTALLEY', 'EXTCRASHSCENE'), ('EXTEASTALLEY', 'EXTEASTROAD'), ('EXTEASTALLEY', 'EXTPEDESTRIANENTRANCE'), ('EXTEASTALLEY', 'EXTPEDESTRIANCUSTOMS'),
    ('EXTPEDESTRIANENTRANCE', 'EXTEASTALLEY'), ('EXTPEDESTRIANENTRANCE', 'EXTPEDESTRIANCUSTOMS'), ('EXTPEDESTRIANENTRANCE', 'EXTEASTVEHENT'),
    ('EXTSOUTHBALCONY', 'EXTPEDESTRIANCUSTOMS'), ('EXTSOUTHBALCONY', 'EXTWESTBALCONY'), ('EXTSOUTHBALCONY', '2FBREAKROOM'), ('EXTSOUTHBALCONY', '1FWAITINGROOM'), ('EXTSOUTHBALCONY', '2FEASTSTAIRS'),
    ('EXTWESTBALCONY', 'EXTSOUTHBALCONY'), ('EXTWESTBALCONY', 'EXTPARKINGLOTENT'), ('EXTWESTBALCONY', 'EXTPARKINGLOTALLEY'), ('EXTWESTBALCONY', '2FSECURITYROOM'), ('EXTWESTBALCONY', '2FARMORYLOCKERS'),
    ('EXTNORTHBALCONY', 'EXTEASTBALCONY'), ('EXTNORTHBALCONY', 'EXTCRASHSCENE'), ('EXTNORTHBALCONY', '2FARCHIVES'),
    ('EXTEASTBALCONY', 'EXTNORTHBALCONY'), ('EXTEASTBALCONY', 'EXTCRASHSCENE'), ('EXTEASTBALCONY', '2FOFFICES'), ('EXTEASTBALCONY', '2FEASTSTAIRS'),
    ('EXTROOF', 'EXTEASTALLEY'), ('EXTROOF', 'EXTCRASHSCENE'), ('EXTROOF', 'EXTVEHICLECUSTOMS'), ('EXTROOF', 'EXTPARKINGLOTALLEY'), ('EXTROOF', 'EXTPARKINGLOTENT'), ('EXTROOF', 'EXTPEDESTRIANCUSTOMS'), ('EXTROOF', '1FWAITINGROOM'),
    ('1FEXITHALLWAY', 'EXTPARKINGLOTALLEY'), ('1FEXITHALLWAY', '1FVENTILATIONROOM'), ('1FEXITHALLWAY', '1FCENTRALSTAIRS'), ('1FEXITHALLWAY', '1FSERVERROOM'),
    ('1FVENTILATIONROOM', '1FEXITHALLWAY'), ('1FVENTILATIONROOM', 'EXTVEHICLECUSTOMS'),
    ('1FSERVERROOM', '1FEXITHALLWAY'), ('1FSERVERROOM', '1FWORKSHOP'),
    ('1FWORKSHOP', '1FSERVERROOM'), ('1FWORKSHOP', '1FMAINLOBBY'),
    ('1FCENTRALSTAIRS', '1FEXITHALLWAY'), ('1FCENTRALSTAIRS', '1FMAINLOBBY'), ('1FCENTRALSTAIRS', '1FCUSTOMSINSPECTION'), ('1FCENTRALSTAIRS', '2FMAINHALLWAY'),
    ('1FCUSTOMSINSPECTION', '1FCENTRALSTAIRS'), ('1FCUSTOMSINSPECTION', '1FCUSTOMSDESK'), ('1FCUSTOMSINSPECTION', '1FMAINLOBBY'), ('1FCUSTOMSINSPECTION', '1FSUPPLYCORRIDOR'),
    ('1FSUPPLYCORRIDOR', '1FCUSTOMSINSPECTION'), ('1FSUPPLYCORRIDOR', '1FDETENTION'), ('1FSUPPLYCORRIDOR', '1FSUPPLYROOM'),
    ('1FDETENTION', '1FSUPPLYCORRIDOR'),
    ('1FSUPPLYROOM', '1FSUPPLYCORRIDOR'), ('1FSUPPLYROOM', 'EXTPARKINGLOTALLEY'),
    ('1FMAINLOBBY', '1FCENTRALSTAIRS'), ('1FMAINLOBBY', '1FWORKSHOP'), ('1FMAINLOBBY', '1FCUSTOMSINSPECTION'), ('1FMAINLOBBY', '1FWAITINGROOM'), ('1FMAINLOBBY', '1FTELLERS'), ('1FMAINLOBBY', '1FBATHROOM'),
    ('1FBATHROOM', '1FMAINLOBBY'),
    ('1FTELLERS', '1FMAINLOBBY'), ('1FTELLERS', 'EXTEASTALLEY'), ('1FTELLERS', '1FWAITINGROOM'),
    ('1FWAITINGROOM', '1FMAINLOBBY'), ('1FWAITINGROOM', '1FTELLERS'), ('1FWAITINGROOM', 'EXTROOF'), ('1FWAITINGROOM', 'EXTSOUTHBALCONY'), ('1FWAITINGROOM', '1FPASSPORTCHECK'), ('1FWAITINGROOM', '1FEASTSTAIRS'), ('1FWAITINGROOM', '2FMAINHALLWAY'),
    ('1FPASSPORTCHECK', '1FWAITINGROOM'), ('1FPASSPORTCHECK', 'EXTPEDESTRIANCUSTOMS'),
    ('1FEASTSTAIRS', '1FWAITINGROOM'), ('1FEASTSTAIRS', '2FEASTSTAIRS'),
    ('2FEASTSTAIRS', '1FEASTSTAIRS'), ('2FEASTSTAIRS', 'EXTSOUTHBALCONY'), ('2FEASTSTAIRS', 'EXTEASTBALCONY'), ('2FEASTSTAIRS', '2FMAINHALLWAY'),
    ('2FMAINHALLWAY', '1FWAITINGROOM'), ('2FMAINHALLWAY', '1FCENTRALSTAIRS'), ('2FMAINHALLWAY', '2FEASTSTAIRS'), ('2FMAINHALLWAY', '2FOFFICES'), ('2FMAINHALLWAY', '2FBREAKROOM'), ('2FMAINHALLWAY', '2FARMORYLOCKERS'),
    ('2FOFFICES', 'EXTEASTBALCONY'), ('2FOFFICES', '2FMAINHALLWAY'), ('2FOFFICES', '2FOFFICEHALLWAY'),
    ('2FOFFICEHALLWAY', '2FOFFICES'), ('2FOFFICEHALLWAY', '2FFOUNTAIN'), ('2FOFFICEHALLWAY', '2FARCHIVES'),
    ('2FFOUNTAIN', '2FOFFICEHALLWAY'),
    ('2FARCHIVES', '2FOFFICEHALLWAY'), ('2FARCHIVES', '2FARMORYLOCKERS'), ('2FARCHIVES', 'EXTNORTHBALCONY'), ('2FARCHIVES', 'EXTVEHICLECUSTOMS'),
    ('2FARMORYLOCKERS', '2FARCHIVES'), ('2FARMORYLOCKERS', 'EXTVEHICLECUSTOMS'), ('2FARMORYLOCKERS', 'EXTWESTBALCONY'), ('2FARMORYLOCKERS', '2FMAINHALLWAY'), ('2FARMORYLOCKERS', '2FARMORYDESK'),
    ('2FARMORYDESK', '2FARMORYLOCKERS'),
    ('2FBREAKROOM', 'EXTSOUTHBALCONY'), ('2FBREAKROOM', '2FMAINHALLWAY'), ('2FBREAKROOM', '2FSECURITYROOM'),
    ('2FSECURITYROOM', 'EXTWESTBALCONY'), ('2FSECURITYROOM', '2FBREAKROOM'),
    ('1FCUSTOMSDESK', '1FCUSTOMSINSPECTION')
], open = True, edge_visited_ATK = 0, edge_visited_DEF = 0, deaths_ATK = 0, deaths_DEF = 0)

#There are some ghost edges that will always be 0 but exist for the testing:
#('2FPILLARROOM', '3FCIGARBALCONY')
#('3FWHITESTAIRS', '3FCOCKTAILLOUNGEENTRANCE')
kafedostoyevsky.add_edges_from([
    ('EXTRIVERDOCKS', 'EXTMAINSTREET'), ('EXTRIVERDOCKS', 'EXTWESTMAINSTREET'),
    ('EXTEASTMAINSTREET', 'EXTMAINSTREET'),
    ('EXTMAINSTREET', 'EXTRIVERDOCKS'), ('EXTMAINSTREET', 'EXTEASTMAINSTREET'), ('EXTMAINSTREET', 'EXTWESTMAINSTREET'), ('EXTMAINSTREET', '1FRECEPTION'),  ('EXTMAINSTREET', '1FDININGROOM'),  ('EXTMAINSTREET', 'EXTTERRACE'), ('EXTMAINSTREET', '2FPILLARROOM'), ('EXTMAINSTREET', 'EXTCAFEROOFTOP'),
    ('EXTWESTMAINSTREET', 'EXTRIVERDOCKS'), ('EXTWESTMAINSTREET', 'EXTMAINSTREET'), ('EXTWESTMAINSTREET', '1FSMALLBAKERY'), ('EXTWESTMAINSTREET', 'EXTBAKERYROOF'), ('EXTWESTMAINSTREET', 'EXTCAFEROOFTOP'), ('EXTWESTMAINSTREET', 'EXTBAKERYPARKING'), ('EXTWESTMAINSTREET', 'EXTCHRISTMASMARKET'),
    ('EXTCHRISTMASMARKET', 'EXTWESTMAINSTREET'), ('EXTCHRISTMASMARKET', 'EXTBAKERYPARKING'), ('EXTCHRISTMASMARKET', 'EXTGARAGE'),
    ('EXTBAKERYPARKING', 'EXTWESTMAINSTREET'), ('EXTBAKERYPARKING', 'EXTCHRISTMASMARKET'), ('EXTBAKERYPARKING', 'EXTGARAGE'), ('EXTBAKERYPARKING', 'EXTBAKERYROOF'), ('EXTBAKERYPARKING', '1FBAKERY'),
    ('EXTGARAGE', 'EXTCHRISTMASMARKET'), ('EXTGARAGE', 'EXTBAKERYROOF'), ('EXTGARAGE', 'EXTBAKERYPARKING'), ('EXTGARAGE', 'EXTBACKALLEY'),
    ('EXTBAKERYROOF', 'EXTBAKERYPARKING'), ('EXTBAKERYROOF', 'EXTBACKALLEY'), ('EXTBAKERYROOF', 'EXTGARAGE'), ('EXTBAKERYROOF', 'EXTCAFEROOFTOP'), ('EXTBAKERYROOF', 'EXTWESTMAINSTREET'), ('EXTBAKERYROOF', '2FMUSEUMENTRANCE'), ('EXTBAKERYROOF', '2FMININGROOM'), ('EXTBAKERYROOF', '3FCIGARLOUNGE'),
    ('EXTBACKALLEY', 'EXTGARAGE'), ('EXTBACKALLEY', 'EXTBAKERYROOF'), ('EXTBACKALLEY', 'EXTCAFEROOFTOP'), ('EXTBACKALLEY', 'EXTPARK'), ('EXTBACKALLEY', 'EXTTERRACE'), ('EXTBACKALLEY', '1FVIPCORRIDOR'), ('EXTBACKALLEY', '2FFIREPLACEHALL'), ('EXTBACKALLEY', '3FWHITECORRIDOR'), ('EXTBACKALLEY', '3FCIGARLOUNGE'),
    ('EXTPARK', 'EXTBACKALLEY'),
    ('EXTTERRACE', 'EXTBACKALLEY'), ('EXTTERRACE', 'EXTCAFEROOFTOP'), ('EXTTERRACE', 'EXTMAINSTREET'), ('EXTTERRACE', '2FPILLARROOM'), ('EXTTERRACE', '3FCOCKTAILBALCONY'), ('EXTTERRACE', '3FCOCKTAILLOUNGE'), ('EXTTERRACE', '3FWHITESTAIRS'),
    ('EXTCAFEROOFTOP', 'EXTTERRACE'), ('EXTCAFEROOFTOP', 'EXTBACKALLEY'), ('EXTCAFEROOFTOP', 'EXTBAKERYROOF'), ('EXTCAFEROOFTOP', 'EXTMAINSTREET'), ('EXTCAFEROOFTOP', '3FBAR'), ('EXTCAFEROOFTOP', 'EXTWESTMAINSTREET'),
    ('1FBAKERY', 'EXTBAKERYPARKING'), ('1FBAKERY', '1FSMALLBAKERY'), ('1FBAKERY', '1FPREPROOM'),
    ('1FPREPROOM', '1FBAKERY'), ('1FPREPROOM', '1FKITCHENCOOKING'),
    ('1FKITCHENCOOKING', '1FPREPROOM'), ('1FKITCHENCOOKING', '1FKITCHENSERVICE'),
    ('1FKITCHENSERVICE', '1FKITCHENCOOKING'), ('1FKITCHENSERVICE', '1FFREEZER'), ('1FKITCHENSERVICE', '1FMAINCORRIDOR'),
    ('1FFREEZER', '1FKITCHENSERVICE'),
    ('1FSMALLBAKERY', '1FBAKERY'), ('1FSMALLBAKERY', 'EXTWESTMAINSTREET'), ('1FSMALLBAKERY', '1FMAINCORRIDOR'),
    ('1FMAINCORRIDOR', '1FSMALLBAKERY'), ('1FMAINCORRIDOR', '1FKITCHENSERVICE'), ('1FMAINCORRIDOR', '1FREDSTAIRS'), ('1FMAINCORRIDOR', '1FCOATCHECK'), ('1FMAINCORRIDOR', '1FBAR'),
    ('1FCOATCHECK', '1FMAINCORRIDOR'), ('1FCOATCHECK', '1FRECEPTION'),
    ('1FRECEPTION', '1FCOATCHECK'), ('1FRECEPTION', 'EXTMAINSTREET'), ('1FRECEPTION', '1FBAR'),
    ('1FBAR', '1FMAINCORRIDOR'), ('1FBAR', '1FRECEPTION'), ('1FBAR', '1FVIPCORRIDOR'), ('1FBAR', '1FDININGROOM'), ('1FBAR', '2FPILLARROOM'),
    ('1FDININGROOM', '1FBAR'), ('1FDININGROOM', 'EXTMAINSTREET'), ('1FDININGROOM', '1FVIPSECTION'),
    ('1FVIPSECTION', '1FDININGROOM'), ('1FVIPSECTION', '1FVIPCORRIDOR'),
    ('1FVIPCORRIDOR', '1FVIPSECTION'), ('1FVIPCORRIDOR', '1FBAR'), ('1FVIPCORRIDOR', 'EXTBACKALLEY'), ('1FVIPCORRIDOR', '1FWHITESTAIRS'),
    ('1FWHITESTAIRS', '2FREADINGROOMCORRIDOR'), ('1FWHITESTAIRS', '1FVIPCORRIDOR'),
    ('2FREADINGROOMCORRIDOR', '1FWHITESTAIRS'), ('2FREADINGROOMCORRIDOR', '2FWHITESTAIRS'), ('2FREADINGROOMCORRIDOR', '2FLAUNDRYROOM'), ('2FREADINGROOMCORRIDOR', '2FREADINGROOM'), ('2FREADINGROOMCORRIDOR', '2FFIREPLACEHALL'), ('2FREADINGROOMCORRIDOR', '2FMAINCORRIDOR'),
    ('2FLAUNDRYROOM', '2FREADINGROOMCORRIDOR'),
    ('2FREADINGROOM', '2FREADINGROOMCORRIDOR'), ('2FREADINGROOM', '2FPILLARROOM'),
    ('2FFIREPLACEHALL', '2FREADINGROOMCORRIDOR'), ('2FFIREPLACEHALL', 'EXTBACKALLEY'), ('2FFIREPLACEHALL', '2FTRAINMUSEUM'),
    ('2FTRAINMUSEUM', '2FFIREPLACEHALL'), ('2FTRAINMUSEUM', '2FMININGROOM'),
    ('2FMININGROOM', '2FTRAINMUSEUM'), ('2FMININGROOM', '2FMAINCORRIDOR'), ('2FMININGROOM', 'EXTBAKERYROOF'), ('2FMININGROOM', '2FMUSEUMENTRANCE'),
    ('1FREDSTAIRS', '1FMAINCORRIDOR'), ('1FREDSTAIRS', '2FMUSEUMENTRANCE'),
    ('2FMUSEUMENTRANCE', '2FMININGROOM'), ('2FMUSEUMENTRANCE', 'EXTBAKERYROOF'), ('2FMUSEUMENTRANCE', '1FREDSTAIRS'), ('2FMUSEUMENTRANCE', '2FREDSTAIRS'),
    ('2FREDSTAIRS', '2FMUSEUMENTRANCE'), ('2FREDSTAIRS', '3FREDSTAIRS'),
    ('2FMAINCORRIDOR', '2FREADINGROOMCORRIDOR'), ('2FMAINCORRIDOR', '2FMININGROOM'), ('2FMAINCORRIDOR', '2FPILLARROOM'),
    ('2FPILLARROOM', '2FMAINCORRIDOR'), ('2FPILLARROOM', 'EXTTERRACE'), ('2FPILLARROOM', 'EXTMAINSTREET'), ('2FPILLARROOM', '1FBAR'), ('2FPILLARROOM', '2FREADINGROOM'), ('2FPILLARROOM', '3FBAR'), ('2FPILLARROOM', '3FCOCKTAILBALCONY'), ('2FPILLARROOM', '3FCIGARBALCONY'),
    ('3FREDSTAIRS', '2FREDSTAIRS'), ('3FREDSTAIRS', '3FCIGARSHOP'),
    ('3FCIGARSHOP', '3FREDSTAIRS'), ('3FCIGARSHOP', '3FCIGARBALCONY'), ('3FCIGARSHOP', '3FBAR'), ('3FCIGARSHOP', '3FCIGARLOUNGE'),
    ('3FCIGARLOUNGE', '3FCIGARSHOP'), ('3FCIGARLOUNGE', 'EXTBAKERYROOF'), ('3FCIGARLOUNGE', 'EXTBACKALLEY'), ('3FCIGARLOUNGE', '3FWHITECORRIDOR'),
    ('3FWHITECORRIDOR', 'EXTBACKALLEY'), ('3FWHITECORRIDOR', '3FWASHROOM'), ('3FWHITECORRIDOR', '3FWHITESTAIRS'), ('3FWHITECORRIDOR', '3FCOCKTAILLOUNGEENTRANCE'), ('3FWHITECORRIDOR', '3FCIGARLOUNGE'),
    ('3FWASHROOM', '3FWHITECORRIDOR'),
    ('2FWHITESTAIRS', '3FWHITESTAIRS'), ('2FWHITESTAIRS', '2FREADINGROOMCORRIDOR'), ('3FWHITESTAIRS', '3FCOCKTAILLOUNGEENTRANCE'),
    ('3FWHITESTAIRS', '2FWHITESTAIRS'), ('3FWHITESTAIRS', 'EXTTERRACE'), ('3FWHITESTAIRS', '3FWHITECORRIDOR'),
    ('3FCOCKTAILLOUNGEENTRANCE', '3FWHITECORRIDOR'), ('3FCOCKTAILLOUNGEENTRANCE', '3FWHITESTAIRS'), ('3FCOCKTAILLOUNGEENTRANCE', '3FCOCKTAILLOUNGE'),
    ('3FCOCKTAILLOUNGE', '3FCOCKTAILLOUNGEENTRANCE'), ('3FCOCKTAILLOUNGE', 'EXTTERRACE'), ('3FCOCKTAILLOUNGE', '3FCOCKTAILBALCONY'), ('3FCOCKTAILLOUNGE', '3FBAR'),
    ('3FCOCKTAILBALCONY', '3FCOCKTAILLOUNGE'), ('3FCOCKTAILBALCONY', 'EXTTERRACE'), ('3FCOCKTAILBALCONY', '2FPILLARROOM'),
    ('3FCIGARBALCONY', '3FCIGARSHOP'), ('3FCIGARBALCONY', '3FBAR'), ('3FCIGARBALCONY', '2FPILLARROOM'),
    ('3FBAR', '2FPILLARROOM'), ('3FBAR', '3FCOCKTAILLOUNGE'), ('3FBAR', '3FCIGARSHOP'), ('3FBAR', '3FCIGARBALCONY'), ('3FBAR', 'EXTCAFEROOFTOP'), ('3FBAR', '3FBARBACKSTORE'),
    ('3FBARBACKSTORE', '3FBAR'), ('3FBARBACKSTORE', '3FBARFREEZER'),
    ('3FBARFREEZER', '3FBARBACKSTORE')
], open = True, edge_visited_ATK = 0, edge_visited_DEF = 0, deaths_ATK = 0, deaths_DEF = 0)

#There are some ghost edges that will always be 0 but exist for the testing:
clubhouse.add_edges_from([

], open = True, edge_visited_ATK = 0, edge_visited_DEF = 0, deaths_ATK = 0, deaths_DEF = 0)

#Add default closed rooms for each map
#Closed includes hatches and soft walls
coastline.add_edges_from([
    ('1FBLUEBAR', '1FSUNRISEBAR'), ('1FBLUEBAR', '1FCOURTYARD'),
    ('1FSUNRISEBAR', '1FBLUEBAR'), ('1FSUNRISEBAR', '2FHOOKAHLOUNGE'),
    ('1FCOURTYARD', '1FBLUEBAR'), ('1FCOURTYARD', '2FBILLIARDSROOM'),
    ('1FMAINLOBBY', '1FSERVICEENTRANCE'), ('1FMAINLOBBY', '2FPENTHOUSE'),
    ('1FSERVICEENTRANCE', '1FMAINLOBBY'),
    ('2FHOOKAHLOUNGE', '2FBILLIARDSROOM'), ('2FHOOKAHLOUNGE', '1FSUNRISEBAR'),
    ('2FBILLIARDSROOM', '2FHOOKAHLOUNGE'), ('2FBILLIARDSROOM', '1FCOURTYARD'),
    ('2FVIPLOUNGE', '2FPENTHOUSE'),
    ('2FPENTHOUSE', '2FVIPLOUNGE'), ('2FPENTHOUSE', '1FMAINLOBBY'),
    ('2FBATHROOM', '2FHALLOFFAME'), ('2FBATHROOM', 'EXTROOFTOP'),
    ('2FHALLOFFAME', '2FBATHROOM'),
    ('EXTROOFTOP', '2FBATHROOM'),
    ('2FSOUTHHALLYWAY', '1FSECURITYROOM'),
    ('1FSECURITYROOM', '2FSOUTHHALLYWAY'),
    ('1FOFFICE', '2FAQUARIUM'),
    ('2FAQUARIUM', '1FOFFICE')
], open = False, edge_visited_ATK = 0, edge_visited_DEF = 0, deaths_ATK = 0, deaths_DEF = 0)

border.add_edges_from([
    ('EXTPARKINGLOTALLEY', '1FDETENTION'),
    ('1FDETENTION', 'EXTPARKINGLOTALLEY'),
    ('1FSUPPLYROOM', '1FCUSTOMSINSPECTION'), ('1FSUPPLYROOM', '1FCENTRALSTAIRS'),
    ('1FCENTRALSTAIRS', '1FSUPPLYROOM'),
    ('1FCUSTOMSINSPECTION', '1FSUPPLYROOM'), ('1FCUSTOMSINSPECTION', '1FPASSPORTCHECK'), ('1FCUSTOMSINSPECTION', '2FSECURITYROOM'),
    ('1FPASSPORTCHECK', '1FCUSTOMSINSPECTION'),
    ('1FVENTILATIONROOM', '1FSERVERROOM'),
    ('1FSERVERROOM', '1FVENTILATIONROOM'), ('1FSERVERROOM', '2FARMORYDESK'),
    ('1FWORKSHOP', '1FBATHROOM'), ('1FWORKSHOP', '2FARCHIVES'),
    ('1FBATHROOM', '1FWORKSHOP'),
    ('EXTCRASHSCENE', '1FTELLERS'),
    ('1FTELLERS', 'EXTCRASHSCENE'), ('1FTELLERS', '2FOFFICES'),
    ('2FBREAKROOM', '1FWAITINGROOM'),
    ('1FWAITINGROOM', '2FBREAKROOM'),
    ('2FSECURITYROOM', '2FMAINHALLWAY'), ('2FSECURITYROOM', '1FCUSTOMSINSPECTION'), ('2FSECURITYROOM', '1FCUSTOMSDESK'),
    ('2FMAINHALLWAY', '2FSECURITYROOM'), ('2FMAINHALLWAY', '2FFOUNTAIN'),
    ('2FFOUNTAIN', '2FMAINHALLWAY'),
    ('2FOFFICES', '2FARCHIVES'), ('2FOFFICES', '1FTELLERS'),
    ('2FARCHIVES', '2FOFFICES'), ('2FARCHIVES', '1FWORKSHOP'),
    ('1FCUSTOMSDESK', '2FSECURITYROOM'),
    ('2FARMORYDESK', '1FSERVERROOM')
], open = False, edge_visited_ATK = 0, edge_visited_DEF = 0, deaths_ATK = 0, deaths_DEF = 0)

kafedostoyevsky.add_edges_from([
    ('EXTCAFEROOFTOP', '3FREDSTAIRS'), ('EXTCAFEROOFTOP', '3FCIGARBALCONY'),
    ('3FCIGARBALCONY', 'EXTCAFEROOFTOP'),
    ('3FREDSTAIRS', 'EXTCAFEROOFTOP'), ('3FREDSTAIRS', '3FCIGARLOUNGE'),
    ('3FCOCKTAILLOUNGE', '2FLAUNDRYROOM'),
    ('2FLAUNDRYROOM', '3FCOCKTAILLOUNGE'), ('2FLAUNDRYROOM', '2FREADINGROOM'),
    ('3FCIGARLOUNGE', '2FTRAINMUSEUM'), ('3FCIGARLOUNGE', '3FBARBACKSTORE'), ('3FCIGARLOUNGE', '3FWASHROOM'), ('3FCIGARLOUNGE', '3FBAR'), ('3FCIGARLOUNGE', '3FREDSTAIRS'),
    ('2FTRAINMUSEUM', '3FCIGARLOUNGE'),
    ('3FCIGARSHOP', '2FMUSEUMENTRANCE'),
    ('2FMUSEUMENTRANCE', '3FCIGARSHOP'), ('2FMUSEUMENTRANCE', '2FPILLARROOM'),
    ('2FFIREPLACEHALL', '1FFREEZER'),
    ('1FFREEZER', '2FFIREPLACEHALL'), ('1FFREEZER', '1FVIPCORRIDOR'),
    ('1FBAKERY', '1FKITCHENCOOKING'),
    ('1FKITCHENCOOKING', '1FBAKERY'), ('1FKITCHENCOOKING', '1FMAINCORRIDOR'),
    ('1FMAINCORRIDOR', '1FKITCHENCOOKING'),
    ('1FVIPCORRIDOR', '1FFREEZER'),
    ('1FBAR', '1FVIPSECTION'),
    ('1FVIPSECTION', '1FBAR'),
    ('2FPILLARROOM', '2FMUSEUMENTRANCE'),
    ('2FREADINGROOM', '2FLAUNDRYROOM'),
    ('3FCOCKTAILLOUNGEENTRANCE', '3FBARBACKSTORE'),
    ('3FBARBACKSTORE', '3FCOCKTAILLOUNGEENTRANCE'), ('3FBARBACKSTORE', '3FWASHROOM'), ('3FBARBACKSTORE', '3FCIGARLOUNGE'),
    ('3FWASHROOM', '3FBARBACKSTORE'), ('3FWASHROOM', '3FCIGARLOUNGE'),
    ('3FBAR', '3FCIGARLOUNGE')
], open = False, edge_visited_ATK = 0, edge_visited_DEF = 0, deaths_ATK = 0, deaths_DEF = 0)

clubhouse.add_edges_from([

], open = False, edge_visited_ATK = 0, edge_visited_DEF = 0, deaths_ATK = 0, deaths_DEF = 0)

#Set node attributes for each map.
nx.set_node_attributes(coastline, 0, 'node_visited_ATK')
nx.set_node_attributes(border, 0, 'node_visited_ATK')
nx.set_node_attributes(kafedostoyevsky, 0, 'node_visited_ATK')
nx.set_node_attributes(clubhouse, 0, 'node_visited_ATK')
nx.set_node_attributes(villa, 0, 'node_visited_ATK')
nx.set_node_attributes(consulate, 0, 'node_visited_ATK')
nx.set_node_attributes(bank, 0, 'node_visited_ATK')
nx.set_node_attributes(coastline, 0, 'node_visited_DEF')
nx.set_node_attributes(border, 0, 'node_visited_DEF')
nx.set_node_attributes(kafedostoyevsky, 0, 'node_visited_DEF')
nx.set_node_attributes(clubhouse, 0, 'node_visited_DEF')
nx.set_node_attributes(villa, 0, 'node_visited_DEF')
nx.set_node_attributes(consulate, 0, 'node_visited_DEF')
nx.set_node_attributes(bank, 0, 'node_visited_DEF')

nx.set_node_attributes(coastline, 0, 'deaths_ATK')
nx.set_node_attributes(border, 0, 'deaths_ATK')
nx.set_node_attributes(kafedostoyevsky, 0, 'deaths_ATK')
nx.set_node_attributes(clubhouse, 0, 'deaths_ATK')
nx.set_node_attributes(villa, 0, 'deaths_ATK')
nx.set_node_attributes(consulate, 0, 'deaths_ATK')
nx.set_node_attributes(bank, 0, 'deaths_ATK')
nx.set_node_attributes(coastline, 0, 'deaths_DEF')
nx.set_node_attributes(border, 0, 'deaths_DEF')
nx.set_node_attributes(kafedostoyevsky, 0, 'deaths_DEF')
nx.set_node_attributes(clubhouse, 0, 'deaths_DEF')
nx.set_node_attributes(villa, 0, 'deaths_DEF')
nx.set_node_attributes(consulate, 0, 'deaths_DEF')
nx.set_node_attributes(bank, 0, 'deaths_DEF')
