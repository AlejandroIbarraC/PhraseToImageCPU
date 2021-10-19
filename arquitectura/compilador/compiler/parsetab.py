
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ADDI B BEQ BGT BGTE BR BREQ BRGT BRGTE CMP CMPI COMMA COMMENT IMM LABEL LD MOV MOVI MUL MULI REG STLL STR STRI SUB SUBI\n    code : body\n    \n    body : instruction body\n         | label body\n    \n    body :\n    \n    label : LABEL\n    \n    instruction : spe_instr\n                | ari_instr\n                | reg_instr\n                | mem_instr\n                | bra_instr\n    \n    ari_instr : ari_instr_name REG COMMA REG COMMA REG\n              | ari_instr_name REG COMMA REG COMMA IMM\n    \n    reg_instr : reg_instr_name REG COMMA REG\n              | reg_instr_name REG COMMA IMM\n    \n    mem_instr : mem_instr_name REG COMMA REG\n              | mem_instr_name REG COMMA IMM\n    \n    bra_instr : bra_instr_name LABEL\n              | bra_ret_instr_name REG\n    \n    spe_instr : STLL\n    \n    ari_instr_name : ADD\n                   | ADDI\n                   | SUB\n                   | SUBI\n                   | MUL\n                   | MULI\n    \n    reg_instr_name : MOV\n                   | MOVI\n                   | CMP\n                   | CMPI\n\n    \n    mem_instr_name : STR\n                   | STRI\n                   | LD\n    \n    bra_instr_name : BGT\n                   | BGTE\n                   | BEQ\n                   | B\n    \n    bra_ret_instr_name : BRGT\n                       | BRGTE\n                       | BREQ\n                       | BR\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,38,39,43,44,49,50,51,52,54,55,],[-4,0,-1,-4,-4,-6,-7,-8,-9,-10,-5,-19,-2,-3,-17,-18,-13,-14,-15,-16,-11,-12,]),'LABEL':([0,3,4,5,6,7,8,9,10,11,15,30,31,32,33,43,44,49,50,51,52,54,55,],[10,10,10,-6,-7,-8,-9,-10,-5,-19,43,-33,-34,-35,-36,-17,-18,-13,-14,-15,-16,-11,-12,]),'STLL':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[11,11,11,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'ADD':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[17,17,17,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'ADDI':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[18,18,18,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'SUB':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[19,19,19,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'SUBI':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[20,20,20,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'MUL':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[21,21,21,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'MULI':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[22,22,22,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'MOV':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[23,23,23,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'MOVI':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[24,24,24,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'CMP':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[25,25,25,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'CMPI':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[26,26,26,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'STR':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[27,27,27,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'STRI':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[28,28,28,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'LD':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[29,29,29,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'BGT':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[30,30,30,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'BGTE':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[31,31,31,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'BEQ':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[32,32,32,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'B':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[33,33,33,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'BRGT':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[34,34,34,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'BRGTE':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[35,35,35,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'BREQ':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[36,36,36,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'BR':([0,3,4,5,6,7,8,9,10,11,43,44,49,50,51,52,54,55,],[37,37,37,-6,-7,-8,-9,-10,-5,-19,-17,-18,-13,-14,-15,-16,-11,-12,]),'REG':([12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,34,35,36,37,45,46,47,53,],[40,41,42,44,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-37,-38,-39,-40,48,49,51,54,]),'COMMA':([40,41,42,48,],[45,46,47,53,]),'IMM':([46,47,53,],[50,52,55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,],[1,]),'body':([0,3,4,],[2,38,39,]),'instruction':([0,3,4,],[3,3,3,]),'label':([0,3,4,],[4,4,4,]),'spe_instr':([0,3,4,],[5,5,5,]),'ari_instr':([0,3,4,],[6,6,6,]),'reg_instr':([0,3,4,],[7,7,7,]),'mem_instr':([0,3,4,],[8,8,8,]),'bra_instr':([0,3,4,],[9,9,9,]),'ari_instr_name':([0,3,4,],[12,12,12,]),'reg_instr_name':([0,3,4,],[13,13,13,]),'mem_instr_name':([0,3,4,],[14,14,14,]),'bra_instr_name':([0,3,4,],[15,15,15,]),'bra_ret_instr_name':([0,3,4,],[16,16,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> body','code',1,'p_code','Syntaxer.py',12),
  ('body -> instruction body','body',2,'p_body','Syntaxer.py',19),
  ('body -> label body','body',2,'p_body','Syntaxer.py',20),
  ('body -> <empty>','body',0,'p_empty','Syntaxer.py',27),
  ('label -> LABEL','label',1,'p_label','Syntaxer.py',34),
  ('instruction -> spe_instr','instruction',1,'p_instruction','Syntaxer.py',47),
  ('instruction -> ari_instr','instruction',1,'p_instruction','Syntaxer.py',48),
  ('instruction -> reg_instr','instruction',1,'p_instruction','Syntaxer.py',49),
  ('instruction -> mem_instr','instruction',1,'p_instruction','Syntaxer.py',50),
  ('instruction -> bra_instr','instruction',1,'p_instruction','Syntaxer.py',51),
  ('ari_instr -> ari_instr_name REG COMMA REG COMMA REG','ari_instr',6,'p_ari_instr','Syntaxer.py',59),
  ('ari_instr -> ari_instr_name REG COMMA REG COMMA IMM','ari_instr',6,'p_ari_instr','Syntaxer.py',60),
  ('reg_instr -> reg_instr_name REG COMMA REG','reg_instr',4,'p_reg_instr','Syntaxer.py',72),
  ('reg_instr -> reg_instr_name REG COMMA IMM','reg_instr',4,'p_reg_instr','Syntaxer.py',73),
  ('mem_instr -> mem_instr_name REG COMMA REG','mem_instr',4,'p_mem_instr','Syntaxer.py',82),
  ('mem_instr -> mem_instr_name REG COMMA IMM','mem_instr',4,'p_mem_instr','Syntaxer.py',83),
  ('bra_instr -> bra_instr_name LABEL','bra_instr',2,'p_bra_instr','Syntaxer.py',92),
  ('bra_instr -> bra_ret_instr_name REG','bra_instr',2,'p_bra_instr','Syntaxer.py',93),
  ('spe_instr -> STLL','spe_instr',1,'p_spe_instr','Syntaxer.py',102),
  ('ari_instr_name -> ADD','ari_instr_name',1,'p_ari_instr_name','Syntaxer.py',111),
  ('ari_instr_name -> ADDI','ari_instr_name',1,'p_ari_instr_name','Syntaxer.py',112),
  ('ari_instr_name -> SUB','ari_instr_name',1,'p_ari_instr_name','Syntaxer.py',113),
  ('ari_instr_name -> SUBI','ari_instr_name',1,'p_ari_instr_name','Syntaxer.py',114),
  ('ari_instr_name -> MUL','ari_instr_name',1,'p_ari_instr_name','Syntaxer.py',115),
  ('ari_instr_name -> MULI','ari_instr_name',1,'p_ari_instr_name','Syntaxer.py',116),
  ('reg_instr_name -> MOV','reg_instr_name',1,'p_reg_instr_name','Syntaxer.py',124),
  ('reg_instr_name -> MOVI','reg_instr_name',1,'p_reg_instr_name','Syntaxer.py',125),
  ('reg_instr_name -> CMP','reg_instr_name',1,'p_reg_instr_name','Syntaxer.py',126),
  ('reg_instr_name -> CMPI','reg_instr_name',1,'p_reg_instr_name','Syntaxer.py',127),
  ('mem_instr_name -> STR','mem_instr_name',1,'p_mem_instr_name','Syntaxer.py',136),
  ('mem_instr_name -> STRI','mem_instr_name',1,'p_mem_instr_name','Syntaxer.py',137),
  ('mem_instr_name -> LD','mem_instr_name',1,'p_mem_instr_name','Syntaxer.py',138),
  ('bra_instr_name -> BGT','bra_instr_name',1,'p_bra_instr_name','Syntaxer.py',146),
  ('bra_instr_name -> BGTE','bra_instr_name',1,'p_bra_instr_name','Syntaxer.py',147),
  ('bra_instr_name -> BEQ','bra_instr_name',1,'p_bra_instr_name','Syntaxer.py',148),
  ('bra_instr_name -> B','bra_instr_name',1,'p_bra_instr_name','Syntaxer.py',149),
  ('bra_ret_instr_name -> BRGT','bra_ret_instr_name',1,'p_bra_ret_instr_name','Syntaxer.py',157),
  ('bra_ret_instr_name -> BRGTE','bra_ret_instr_name',1,'p_bra_ret_instr_name','Syntaxer.py',158),
  ('bra_ret_instr_name -> BREQ','bra_ret_instr_name',1,'p_bra_ret_instr_name','Syntaxer.py',159),
  ('bra_ret_instr_name -> BR','bra_ret_instr_name',1,'p_bra_ret_instr_name','Syntaxer.py',160),
]
