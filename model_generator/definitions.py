#the language and the technology field with be tokenized
#commit count will be nomalized to 100 is it greater than 100, 100 == 1
template_data = """
   {
      "classifications":"intermediate,novice,disqualified,expert",
      "languages": "A#,A-0 System,A+,A++,ABAP,ABC,ABC ALGOL,ABSET,ABSYS,ACC,Accent,Ace DASL,ACL2,ACT-III,Action!,ActionScript,Ada,Adenine,Agda,Agilent VEE,Agora,AIMMS,Alef,ALF,ALGOL 58,ALGOL 60,ALGOL 68,ALGOL W,Alice,Alma-0,AmbientTalk,Amiga E,AMOS,AMPL,Apex,APL,App Inventor for Android's visual block language,AppleScript,Arc,ARexx,Argus,AspectJ,Assembly language,ATS,Ateji PX,AutoHotkey,Autocoder,AutoIt,AutoLISP / Visual LISP,Averest,AWK,Axum,B,Babbage,Bash,BASIC,bc,BCPL,BeanShell,Batch (Windows/Dos),Bertrand,BETA,Bigwig,Bistro,BitC,BLISS,Blockly,BlooP,Blue,Boo,Boomerang,shell,BREW,BPEL,C,C--,C++,C#,C/AL,Caché ObjectScript,C Shell,Caml,Cayenne,CDuce,Cecil,Cel,Cesil,Ceylon,CFEngine,CFML,Cg,Ch,Chapel,CHAIN,Charity,Charm,Chef,CHILL,CHIP-8,chomski,ChucK,CICS,Cilk,Citrine,CL,Claire,Clarion,Clean,Clipper,CLIST,Clojure,CLU,CMS-2,COBOL – ISO/IEC 1989,Cobra,CODE,CoffeeScript,ColdFusion,COMAL,Combined Programming Language (CPL),COMIT,Common Intermediate Language (CIL),Common Lisp (also known as CL),COMPASS,Component Pascal,Constraint Handling Rules (CHR),Converge,Cool,Coq,Coral 66,Corn,CorVision,COWSEL,CPL,Cryptol,csh,Csound,CSP,CUDA,Curl,Curry,Cyclone,Cython,D,DASL (Datapoint's Advanced Systems Language),DASL (Distributed Application Specification Language),Dart,DataFlex,Datalog,DATATRIEVE,dBase,dc,DCL,Deesel (formerly G),Delphi,DinkC,DIBOL,Dog,Draco,DRAKON,Dylan,DYNAMO,E,E#,Ease,Easy PL/I,Easy Programming Language,EASYTRIEVE PLUS,ECMAScript,Edinburgh IMP,EGL,Eiffel,ELAN,Elixir,Elm,Emacs Lisp,Emerald,Epigram,EPL,Erlang,es,Escher,ESPOL,Esterel,Etoys,Euclid,Euler,Euphoria,EusLisp Robot Programming Language,CMS EXEC (EXEC),EXEC 2,Executable UML,F,F#,Factor,Falcon,Fantom,FAUST,FFP,Fjölnir,FL,Flavors,Flex,FlooP,FLOW-MATIC,FOCAL,FOCUS,FOIL,FORMAC,@Formula,Forth,Fortran – ISO/IEC 1539,Fortress,FoxBase,FoxPro,FP,FPr,Franz Lisp,Frege,F-Script,G,Game Maker Language,GameMonkey Script,GAMS,GAP,G-code,Genie,GDL,GJ,GEORGE,GLSL,GNU E,GM,Go,Go!,GOAL,Gödel,Godiva,Golo,GOM (Good Old Mad),Google Apps Script,Gosu,GOTRAN,GPSS,GraphTalk,GRASS,Groovy,Hack,HAL/S,Hamilton C shell,Harbour,Hartmann pipelines,Haskell,Haxe,High Level Assembly,HLSL,Hop,Hopscotch,Hope,Hugo,Hume,HyperTalk,IBM Basic assembly language,IBM HAScript,IBM Informix-4GL,IBM RPG,ICI,Icon,Id,IDL,Idris,IMP,Inform,Io,Ioke,IPL,IPTSCRAE,ISLISP,ISPF,ISWIM,J,J#,J++,JADE,Jako,JAL,Janus,Janus,JASS,Java,JavaScript,JCL,JEAN,Join Java,JOSS,Joule,JOVIAL,Joy,JScript,JScript .NET,JavaFX Script,Julia,Jython,K,Kaleidoscope,Karel,Karel++,KEE,Kixtart,Klerer-May System,KIF,Kojo,Kotlin,KRC,KRL,KUKA Robot Language),KRYPTON,ksh,L,L# .NET,LabVIEW,Ladder,Lagoona,LANSA,Lasso,LaTeX,Lava,LC-3,Leda,Legoscript,LIL,LilyPond,Limbo,Limnor,LINC,Lingo,LIS,LISA,Lisaac,Lisp – ISO/IEC 13816,Lite-C,Lithe,Little b,Logo,Logtalk,LotusScript,LPC,LSE,LSL,LiveCode,LiveScript,Lua,Lucid,Lustre,LYaPAS,Lynx,M2001,MarsCode (programming language),M4,M#,Machine code,MAD (Michigan Algorithm Decoder),MAD/I,Magik,Magma,make,Maple,MAPPER now part of BIS,MARK-IV now VISION:BUILDER,Mary,MASM Microsoft Assembly x86,MATH-MATIC,Mathematica,MATLAB,Maxima (see also,Macsyma ),Max (Max Msp – Graphical Programming Environment),MaxScript internal language 3D Studio Max,Maya (MEL),MDL,Mercury,Mesa,Metacard,Metafont,Microcode,MicroScript,MIIS,MillScript,MIMIC,Mirah,Miranda,MIVA Script,ML,Moby,Model 204,Modelica,Modula,Modula-2,Modula-3,Mohol,MOO,Mortran,Mouse,MPD,CIL,MSL,MUMPS,Mystic Programming Language (MPL),NASM,Napier88,Neko,Nemerle,nesC,NESL,Net.Data,NetLogo,NetRexx,NewLISP,NEWP,Newspeak,NewtonScript,NGL,Nial,Nice,Nickle,Nim,NPL,Not eXactly C (NXC),Not Quite C (NQC),NSIS,Nu,NWScript,NXT-G,o:XML,Oak,Oberon,OBJ2,Object Lisp,ObjectLOGO,Object REXX,Object Pascal,Objective-C,Objective-J,Obliq,OCaml,occam,occam-π,Octave,OmniMark,Onyx,Opa,Opal,OpenCL,OpenEdge ABL,OPL,OPS5,OptimJ,Orc,ORCA/Modula-2,Oriel,Orwell,Oxygene,Oz,P′′,P#,ParaSail (programming language),PARI/GP,Pascal – ISO 7185,PCASTL,PCF,PEARL,PeopleCode,Perl,PDL,Perl6,Pharo,PHP,Phrogram,Pico,Picolisp,Pict,Pike,PIKT,PILOT,Pipelines,Pizza,PL-11,PL/0,PL/B,PL/C,PL/I – ISO 6160,PL/M,PL/P,PL/SQL,PL360,PLANC,Plankalkül,Planner,PLEX,PLEXIL,Plus,POP-11,PostScript,PortablE,Powerhouse,PowerBuilder – 4GL GUI applcation generator from Sybase,PowerShell,PPL,Processing,Processing.js,Prograph,PROIV,Prolog,PROMAL,Promela,PROSE modeling language,PROTEL,ProvideX,Pro*C,Pure,Python,Q (equational programming language),Q (programming language from Kx Systems),Qalb,QtScript,QuakeC,QPL,R,R++,Racket,RAPID,Rapira,Ratfiv,Ratfor,rc,REBOL,Red,Redcode,REFAL,Reia,Revolution,REXX,Rlab,ROOP,RPG,RPL,RSL,RTL/2,Ruby,RuneScript,Rust,S,S2,S3,S-Lang,S-PLUS,SA-C,SabreTalk,SAIL,SALSA,SAM76,SAS,SASL,Sather,Sawzall,SBL,Scala,Scheme,Scilab,Scratch,Script.NET,Sed,Seed7,Self,SenseTalk,SequenceL,SETL,SIMPOL,SIGNAL,SiMPLE,SIMSCRIPT,Simula,Simulink,SISAL,SLIP,SMALL,Smalltalk,Small Basic,SML,Snap!,SNOBOL (,SPITBOL ),Snowball,SOL,Span,SPARK,Speedcode,SPIN,SP/k,SPS,SQR,Squeak,Squirrel,SR,S/SL,Stackless Python,Starlogo,Strand,Stata,Stateflow,Subtext,SuperCollider,SuperTalk,Swift (Apple programming language),Swift (parallel scripting language),SYMPL,SyncCharts,SystemVerilog,T,TACL,TACPOL,TADS,TAL,Tcl,Tea,TECO,TELCOMP,TeX,TEX,TIE,Timber,TMG,compiler-compiler,Tom,TOM,TouchDevelop,Topspeed,TPU,Trac,TTM,T-SQL,TTCN,Turing,TUTOR,TXL,TypeScript,Turbo C++,Ubercode,UCSD Pascal,Umple,Unicon,Uniface,UNITY,Unix shell,UnrealScript,Vala,Visual DataFlex,Visual DialogScript,Visual Fortran,Visual FoxPro,Visual J++,Visual J#,Visual Objects,Visual Prolog,VSXu,vvvv,WATFIV,WATFOR,WebDNA,WebQL,Whiley,Windows PowerShell,Winbatch,Wolfram Language,Wyvern,X++,X#,X10,XBL,XC (exploits,XMOS architecture ),xHarbour,XL,Xojo,XOTcl,XPL,XPL0,XQuery,XSB,XSLT – see,XPath,Xtend,Yorick,YQL,Z notation,Zeno,ZOPL,Zsh,ZPL,none",
      "technology": "redis,mongodb,mssql,spring,spring-boot,apache-camel,nodejs,angulajs,reactjs,none",
      "params":{
         "na":-1,
         "never":730,
         "max_commit":100,
         "max_churn":5
      },
      "disqualified":[{
         "language": "none",
         "library": "none",
         "commit_count": [0,100],
         "days_since_last_commit": [0,730],
         "code_churn": [0,5],
         "classification": "disqualified"
      }],
      "novice":[{
         "language": "java",
         "library": "none",
         "commit_count":[1, 3],
         "days_since_last_commit": [730, 730],
         "code_churn": [0,1],
         "classification": "novice"        
      },
      {
         "language": "javascript",
         "library": "none",
         "commit_count":[1, 3],
         "days_since_last_commit": [730, 730],
         "code_churn": [0,1],
         "classification": "novice"            
      }],
      "intermediate":[{
         "language": "java",
         "library": "none",
         "commit_count":[3, 10],
         "days_since_last_commit": [365, 730],
         "code_churn": [1, 4],
         "classification": "intermediate"                    
      },{
         "language": "javascript",
         "library": "none",
         "commit_count":[3, 10],
         "days_since_last_commit": [365, 730],
         "code_churn": [1, 4],
         "classification": "intermediate"             
      }],
      "expert":[{
         "language": "java",
         "library": "redis,mongodb,spring-boot",
         "commit_count":[10, 100],
         "days_since_last_commit": [0, 365],
         "code_churn": [5, 5],
         "classification": "expert"
      },
      {
         "language": "javascript",
         "library": "reactjs,nodejs,angulajs",
         "commit_count":[10, 100],
         "days_since_last_commit": [0, 365],
         "code_churn": [5, 5],
         "classification": "expert"
      }]
   }         
"""

def gen_classification_data(classification_template, libraries_dict, language_dict, classifications_dict):
       
   outputdata = []
   language_val = language_dict[classification_template['language'].lower()]
   classification = classifications_dict[classification_template['classification'].lower()]

   libraries = []
   _libraries = classification_template['library'].lower().split(",")
   for lib in _libraries:
      if lib in libraries_dict:
         token = libraries_dict[lib] 
         libraries.append(token)  

   if len(libraries) == 0:
      libraries.append(libraries_dict["none"]) 

   worked_libraries_of_interest = 1
   if len(libraries) == 1 and libraries[0] == libraries_dict["none"]:
      worked_libraries_of_interest = 0

   #
   for lib_val in libraries:
      entry = []
      for day in range(classification_template['days_since_last_commit'][0], classification_template['days_since_last_commit'][1] + 1):
         for commit in range(classification_template['commit_count'][0], classification_template['commit_count'][1] + 1):
            for code_churn in range(classification_template['code_churn'][0], classification_template['code_churn'][1] + 1):
               entry = [language_val, lib_val, worked_libraries_of_interest, commit, day, code_churn, classification]                                          
               outputdata.append(entry)

   return outputdata

import numpy as np

def softmax(x, max):
   max_n = np.max([10])
   e_x = np.exp(x - max_n)
   return e_x / e_x.sum()

def normalize(x, max):
   _min = np.min(x)
   _max = np.max([10])
   e_x = (x - _min) / (_max - _min)
   return e_x 

def squash(x, max):
   _min = np.min(x)
   _max = np.max([10])
   e_x = []
   for _x in x:
      e_x.append(1 - (1 / _x))
   
   return e_x 

def map_reduce(x, max):
   
   _min = np.min(x)
   _max = np.max([10])
   e_x = (x - _min) / (_max - _min)
   return e_x 


# val= softmax([1,2,3,4,5,6,7,8,9,10,11], 10)
# print("softmax value:", val)

# nval= normalize([1,2,3,4,5,6,7,8,9,10,11], 10)
# print("normalization value:", nval)

# nval= squash([10,11,999], 10)
# print("squash value:", nval)

# nval= map_reduce([1,2,3,4,5,6,7,8,9,10,11], 10)
# print("map reduce value:", nval)