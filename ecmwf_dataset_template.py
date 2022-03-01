"""
*******************************************************************************
Data Structures for COSMO and WRF ecmwfapi requests
Dominik Strebel, Empa
*******************************************************************************
"""

SUPPORTED_MODELS = ["era5", "interim"]

"""
*******************************************************************************
ERA 5 and interim MARS default params.
*******************************************************************************
"""
grid = "5/100/-2/108"
res = "0.25/0.25"
date = "2014-02-01/to/2014-02-28"
times_era5="00:00:00/03:00:00/06:00:00/09:00:00/12:00:00/15:00:00/18:00:00/21:00:00"
times_erainterim = "00:00:00/06:00:00/12:00:00/18:00:00"
cosmo_sfc_params = "039/040/041/042/043/129/134/139/141/170/172/183/198/235/236/238"
cosmo_sfc_interim_params = "039/040/041/042/129/134/139/141/170/172/183/198/235/236/238"
cosmo_ml_params = "075/076/130/131/132/133/152/203.200/246/247"
cosmo_pl_params = "129"
wrf_sfc_params = "msl/skt/2t/10u/10v/2d/z/lsm/sst/ci/sd/stl1/stl2/stl3/stl4/swvl1/swvl2/swvl3/swvl4"
wrf_ml_params = "129/130/131/132/133/152"
mod_levs = "all"
cosmo_era5_sfc_file = "ERA5_cosmo_sfc.grb"
cosmo_era5_ml_file = "ERA5_cosmo_ml.grb"
cosmo_era5_pl_file = "ERA5_cosmo_pl.grb"
cosmo_era5_out_file = "ERA5_cosmo_merged.grb"
wrf_era5_sfc_file = "ERA5_wrf_sfc.grb"
wrf_era5_ml_file = "ERA5_wrf_ml.grb"
wrf_era5_out_file = "ERA5_wrf_merged.grb"


cosmo_interim_sfc_file = "ERA-interim_cosmo_sfc.grb"
cosmo_interim_ml_file = "ERA-interim_cosmo_ml.grb"
cosmo_interim_pl_file = "ERA-interim_cosmo_pl.grb"
cosmo_interim_out_file = "ERA-interim_cosmo_merged.grb"
wrf_interim_sfc_file = "ERA-interim_sfc.grb"
wrf_interim_ml_file = "ERA-interim_wrf_ml.grb"
wrf_interim_out_file = "ERA-interim_wrf_merged.grb"

cosmo_era5_infile_list = [cosmo_era5_sfc_file,
                          cosmo_era5_ml_file, cosmo_era5_pl_file]
wrf_era5_infile_list = [wrf_era5_sfc_file, wrf_era5_ml_file]

cosmo_interim_infile_list = [cosmo_interim_sfc_file,
                             cosmo_interim_ml_file, cosmo_interim_pl_file]
wrf_interim_infile_list = [wrf_interim_sfc_file, wrf_interim_ml_file]

"""
*******************************************************************************
COSMO DICS
*******************************************************************************
"""


cosmo_era5_sfc_dic = {
    'stream': 'oper',
    'class': 'ea',
    'dataset': 'era5',
    'date': date,
    'levtype': "sfc",
    'param': cosmo_sfc_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'expver': "1",
    'time': times_era5,
    'target': cosmo_era5_sfc_file
}
cosmo_era5_pl_dic = {
    'stream': 'oper',
    'class': 'ea',
    'dataset': 'era5',
    'date': date,
    'levtype': "pl",
    'param': cosmo_pl_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'expver': "1",
    'time': times_era5,
    'target': cosmo_era5_pl_file
}
cosmo_era5_ml_dic = {
    'stream': 'oper',
    'class': 'ea',
    'dataset': 'era5',
    'date': date,
    'levtype': "ml",
    'levelist': mod_levs,
    'param': cosmo_ml_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'expver': "1",
    'time': times_era5,
    'target': cosmo_era5_ml_file
}


cosmo_era5_dic_list = [cosmo_era5_sfc_dic,
                       cosmo_era5_ml_dic, cosmo_era5_pl_dic]


cosmo_interim_sfc_dic = {
    'stream': 'oper',
    'class': 'ei',
    'dataset': 'interim',
    'step'      : "0",
    'date': date,
    'levtype': "sfc",
    'param': cosmo_sfc_interim_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'time': times_erainterim,
    'target': cosmo_interim_sfc_file
}
cosmo_interim_pl_dic = {
    'stream': 'oper',
    'class': 'ei',
    'step'      : "0",
    'dataset': 'interim',
    'date': date,
    'levtype': "pl",
    'param': cosmo_pl_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'time': times_erainterim,
    'target': cosmo_interim_pl_file
}
cosmo_interim_ml_dic = {
    'stream': 'oper',
    'class': 'ei',
    'dataset': 'interim',
    'date': date,
    'step': "0",
    'levtype': "ml",
    'levelist': mod_levs,
    'param': cosmo_ml_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'time': times_erainterim,
    'target': cosmo_interim_ml_file
}


cosmo_interim_dic_list = [cosmo_interim_sfc_dic,
                          cosmo_interim_ml_dic, cosmo_interim_pl_dic]
"""
******************************************************************************
WRF DICS
******************************************************************************
"""


wrf_era5_sfc_dic = {
    'stream': 'oper',
    'class': 'ea',
    'dataset': 'era5',
    'date': date,
    'levtype': "sfc",
    'param': wrf_sfc_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'expver': "1",
    'time': times_era5,
    'target': wrf_era5_sfc_file
}

wrf_era5_ml_dic = {
    'stream': 'oper',
    'class': 'ea',
    'dataset': 'era5',
    'date': date,
    'levtype': "ml",
    'levelist': mod_levs,
    'param': wrf_ml_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'expver': "1",
    'time': times_era5,
    'target': wrf_era5_ml_file
}

wrf_era5_dic_list = [wrf_era5_sfc_dic, wrf_era5_ml_dic]


wrf_interim_sfc_dic = {
    'stream': 'oper',
    'class': 'ei',
    'dataset': 'interim',
    'date': date,
    'levtype': "sfc",
    'param': wrf_sfc_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'expver': "1",
    'time': times_erainterim,
    'target': wrf_interim_sfc_file
}

wrf_interim_ml_dic = {
    'stream': 'oper',
    'class': 'ei',
    'dataset': 'interim',
    'date': date,
    'levtype': "ml",
    'levelist': mod_levs,
    'param': wrf_ml_params,
    'area': grid,
    'grid': res,
    'type': "an",
    'expver': "1",
    'time': times_erainterim,
    'target': wrf_interim_ml_file
}

wrf_interim_dic_list = [wrf_interim_sfc_dic, wrf_interim_ml_dic]


"""
*****************************************************************************
VTABLE  for wrf
"""

VTABLE = """GRIB | Level| Level| Level| metgrid  |  metgrid | metgrid                                  |
Code | Code |   1  |   2  | Name     |  Units   | Description                              |
-----+------+------+------+----------+----------+------------------------------------------+
 130 | 109  |   *  |      | TT       | K        | Temperature                              |
 131 | 109  |   *  |      | UU       | m s-1    | U                                        |
 132 | 109  |   *  |      | VV       | m s-1    | V                                        |
 133 | 109  |   *  |      | SPECHUMD | kg kg-1  | Specific humidity                        |
 157 | 109  |   *  |      | RHUM     | %        | Relative humidity                        |
 152 | 109  |   *  |      | LOGSFP   | Pa       | Log surface pressure                     |
 165 |  1   |   0  |      | UU       | m s-1    | U                                        | At 10 m
 166 |  1   |   0  |      | VV       | m s-1    | V                                        | At 10 m
 167 |  1   |   0  |      | TT       | K        | Temperature                              | At 2 m
 168 |  1   |   0  |      | DEWPT    | K        |                                          | At 2 m
     |  1   |   0  |      | RH       | %        | Relative Humidity at 2 m                 | At 2 m
 172 |  1   |   0  |      | LANDSEA  | 0/1 Flag | Land/Sea flag                            |
 129 |  1   |   0  |      | SOILGEO  | m2 s-2   |                                          |
     |  1   |   0  |      | SOILHGT  | m        | Terrain field of source analysis         |
 134 |  1   |   0  |      | PSFC     | Pa       | Surface Pressure                         |
 134 | 109  |   1  |      | PSFCH    | Pa       | P                                        |
 151 |  1   |   0  |      | PMSL     | Pa       | Sea-level Pressure                       |
 235 |  1   |   0  |      | SKINTEMP | K        | Sea-Surface Temperature                  |
  31 |  1   |   0  |      | SEAICE   | fraction | Sea-Ice-Fraction                         |
  34 |  1   |   0  |      | SST      | K        | Sea-Surface Temperature                  |
  33 |  1   |   0  |      | SNOW_DEN | kg m-3   |                                          |
 141 |  1   |   0  |      | SNOW_EC  | m        |                                          |
     |  1   |   0  |      | SNOW     | kg m-2   |Water Equivalent of Accumulated Snow Depth|
     |  1   |   0  |      | SNOWH    | m        | Physical Snow Depth                      |
 139 | 112  |   0  |   7  | ST000007 | K        | T of 0-7 cm ground layer                 |
 170 | 112  |   7  |  28  | ST007028 | K        | T of 7-28 cm ground layer                |
 183 | 112  |  28  | 100  | ST028100 | K        | T of 28-100 cm ground layer              |
 236 | 112  | 100  | 255  | ST100289 | K        | T of 100-289 cm ground layer             |
  39 | 112  |   0  |   7  | SM000007 | m3 m-3   | Soil moisture of 0-7 cm ground layer     |
  40 | 112  |   7  |  28  | SM007028 | m3 m-3   | Soil moisture of 7-28 cm ground layer    |
  41 | 112  |  28  | 100  | SM028100 | m3 m-3   | Soil moisture of 28-100 cm ground layer  |
  42 | 112  | 100  | 255  | SM100289 | m3 m-3   | Soil moisture of 100-289 cm ground layer |
-----+------+------+------+----------+----------+------------------------------------------+
#
#  For use with ERA-interim and ERA-5 model-level output.
#
#  Grib codes are from Table 128
#  http://www.ecmwf.int/services/archive/d/parameters/order=grib_parameter/table=128/
#
# snow depth is converted to the proper units in rrpr.F
#
#  For ERA-interim data at NCAR, use the ml (sc and uv) and sfc sc files.
"""


"""
****************************************************************************
ECMWF Coefficients for pressure levels
*****************************************************************************
"""

ECMWF_COEFFS_130 = """0 0.000000 0.00000000
1 2.000365 0.00000000
2 3.102241 0.00000000
3 4.666084 0.00000000
4 6.827977 0.00000000
5 9.746966 0.00000000
6 13.605424 0.00000000
7 18.608931 0.00000000
8 24.985718 0.00000000
9 32.985710 0.00000000
10 42.879242 0.00000000
11 54.955463 0.00000000
12 69.520576 0.00000000
13 86.895882 0.00000000
14 107.415741 0.00000000
15 131.425507 0.00000000
16 159.279404 0.00000000
17 191.338562 0.00000000
18 227.968948 0.00000000
19 269.539581 0.00000000
20 316.420746 0.00000000
21 368.982361 0.00000000
22 427.592499 0.00000000
23 492.616028 0.00000000
24 564.413452 0.00000000
25 643.339905 0.00000000
26 729.744141 0.00000000
27 823.967834 0.00000000
28 926.344910 0.00000000
29 1037.201172 0.00000000
30 1156.853638 0.00000000
31 1285.610352 0.00000000
32 1423.770142 0.00000000
33 1571.622925 0.00000000
34 1729.448975 0.00000000
35 1897.519287 0.00000000
36 2076.095947 0.00000000
37 2265.431641 0.00000000
38 2465.770508 0.00000000
39 2677.348145 0.00000000
40 2900.391357 0.00000000
41 3135.119385 0.00000000
42 3381.743652 0.00000000
43 3640.468262 0.00000000
44 3911.490479 0.00000000
45 4194.930664 0.00000000
46 4490.817383 0.00000000
47 4799.149414 0.00000000
48 5119.895020 0.00000000
49 5452.990723 0.00000000
50 5798.344727 0.00000000
51 6156.074219 0.00000000
52 6526.946777 0.00000000
53 6911.870605 0.00000000
54 7311.869141 0.00000000
55 7727.412109 0.00000700
56 8159.354004 0.00002400
57 8608.525391 0.00005900
58 9076.400391 0.00011200
59 9562.682617 0.00019900
60 10065.978516 0.00034000
61 10584.631836 0.00056200
62 11116.662109 0.00089000
63 11660.067383 0.00135300
64 12211.547852 0.00199200
65 12766.873047 0.00285700
66 13324.668945 0.00397100
67 13881.331055 0.00537800
68 14432.139648 0.00713300
69 14975.615234 0.00926100
70 15508.256836 0.01180600
71 16026.115234 0.01481600
72 16527.322266 0.01831800
73 17008.789062 0.02235500
74 17467.613281 0.02696400
75 17901.621094 0.03217600
76 18308.433594 0.03802600
77 18685.718750 0.04454800
78 19031.289062 0.05177300
79 19343.511719 0.05972800
80 19620.042969 0.06844800
81 19859.390625 0.07795800
82 20059.931641 0.08828600
83 20219.664062 0.09946200
84 20337.863281 0.11150500
85 20412.308594 0.12444800
86 20442.078125 0.13831300
87 20425.718750 0.15312500
88 20361.816406 0.16891000
89 20249.511719 0.18568900
90 20087.085938 0.20349100
91 19874.025391 0.22233300
92 19608.572266 0.24224400
93 19290.226562 0.26324200
94 18917.460938 0.28535400
95 18489.707031 0.30859800
96 18006.925781 0.33293900
97 17471.839844 0.35825400
98 16888.687500 0.38436300
99 16262.046875 0.41112500
100 15596.695312 0.43839100
101 14898.453125 0.46600300
102 14173.324219 0.49380000
103 13427.769531 0.52161900
104 12668.257812 0.54930100
105 11901.339844 0.57669200
106 11133.304688 0.60364800
107 10370.175781 0.63003600
108 9617.515625 0.65573600
109 8880.453125 0.68064300
110 8163.375000 0.70466900
111 7470.343750 0.72773900
112 6804.421875 0.74979700
113 6168.531250 0.77079800
114 5564.382812 0.79071700
115 4993.796875 0.80953600
116 4457.375000 0.82725600
117 3955.960938 0.84388100
118 3489.234375 0.85943200
119 3057.265625 0.87392900
120 2659.140625 0.88740800
121 2294.242188 0.89990000
122 1961.500000 0.91144800
123 1659.476562 0.92209600
124 1387.546875 0.93188100
125 1143.250000 0.94086000
126 926.507812 0.94906400
127 734.992188 0.95655000
128 568.062500 0.96335200
129 424.414062 0.96951300
130 302.476562 0.97507800
131 202.484375 0.98007200
132 122.101562 0.98454200
133 62.781250 0.98850000
134 22.835938 0.99198400
135 3.757813 0.99500300
136 0.000000 0.99763000
137 0.000000 1.00000000
"""

"""
******************************************************************************
COSMO int2lm namelist
******************************************************************************
"""
INT2LM_INPUT = """&CONTRL
   ydate_ini='$ydate_ini',
   yinput_model='IFS',
   hstart=0.0,
   hstop=$hstop,
   hincbound=3.0,
   nincwait=30, 
   nmaxwait=300,
   nprocx= 6,
   nprocy= 10, 
   nprocio = 0,
   lasync_io = .FALSE.,
   linitial=.TRUE.,
   lboundaries=.TRUE.,
   lforest=.TRUE.,   
   lsso = .TRUE.,
   lradtopo=.FALSE.,
   llake = .FALSE.,
   lbdclim=.TRUE.,
   idbg_level = 100,
   ltime_mean=.TRUE.,
   lvertwind_ini=.TRUE.,
   lvertwind_bd=.TRUE.,
   lprog_qi=.TRUE.,  
   lprog_qr_qs=.FALSE.,
   lprog_qg=.FALSE.,  
   lmulti_layer_lm=.TRUE.,
   lmulti_layer_in=.FALSE.,
   lprog_rho_snow=.FALSE.
   luse_t_skin=.TRUE.,
   lfilter_oro=.FALSE.,
   lfilter_pp=.TRUE.,
   eps_filter=0.1,
   norder_filter=5,
   ilow_pass_oro=4,   
   numfilt_oro=1,   
   ilow_pass_xso=5, 
   numfilt_xso=1,
   lxso_first=.FALSE.,
   rxso_mask=750.0,
   rfill_valley=0.0, 
   ifill_valley=7,   
   l_topo_z=.FALSE., 
   llbc_smooth=.TRUE.,
   nlbc_smooth=10,
   l_smi=.TRUE.,
/

&GRID_IN
  pcontrol_fi     = 30000.,
  ie_in_tot       = $grid_in_i, 
  je_in_tot       = $grid_in_j, 
  ke_in_tot       = 137,
  pollat_in       = 90.0, 
  pollon_in       = 180.0, 
  startlat_in_tot = $start_lat,
  startlon_in_tot = $start_lon,
  dlat_in         = $dlat,
  dlon_in         = $dlon,
/
&LMGRID
  startlat_tot = 0.7,
  startlon_tot = 103.0, 
  pollat       = 90.0, 
  pollon       = 180.0, 
  dlon         = 0.0025, 
  dlat         = 0.0025,
  ielm_tot     = 720,
  jelm_tot     = 560,
  kelm_tot     = 60,
  ivctype = 2,
  vcflat = 11357.0,
  vcoord_d=23588.50,22395.93,21304.04,   20307.39,   19399.95,
     18574.03,   17821.88,   17135.64,   16507.79,   15930.60,
     15396.52,   14897.86,   14427.98,   13981.10,   13551.52,
     13133.53,   12721.37,   12312.04,   11900.03,   11485.37,
     11068.19,   10648.54,   10226.48,    9802.09,    9375.43,
      8946.58,    8515.59,    8082.55,    7647.52,    7210.55,
      6771.96,    6332.38,    5896.41,    5468.04,    5050.84,
      4647.96,    4261.91,    3893.26,    3542.15,    3208.52,
      2892.23,    2593.71,    2312.95,    2049.75,    1803.89,
      1575.57,    1364.68,    1170.90,     993.84,     833.44,
       689.53,     561.52,     448.82,     350.95,     267.55,
       197.67,     137.23,      87.33,      48.44,      20.00, 0.0,
/
&DATABASE
/
&DATA
  ncenter          = 215,
  nprocess_ini     = 131,
  nprocess_bd      = 132,
  ymode_write      = 'w',
  yinput_type      = 'analysis',
  ie_ext           = 1600, 
  je_ext           = 1600,
  ylmext_form_read = 'ncdf',
  ylmext_lfn       = 'domain2018041211137.nc',
  ylmext_cat       = '/mnt/data/std/Singapore/int2lm/extpar'
  yinext_form_read = "apix",
  yinext_lfn       = '$eas_first',
  yinext_cat       = '$input_dir',
  yin_form_read    = 'apix',
  yin_cat          = '$input_dir',
  ylm_cat          = '$output_dir',
  ylm_form_write   = "ncdf",
/
&PRICTR
  igp_tot = 36, 40, 48, 44, 48, 85, 77,
  jgp_tot = 30, 94, 38, 26, 26, 96, 12,
  lchkin  = .TRUE., 
  lchkout = .TRUE.,
  lprgp   = .FALSE.,
/"""

"""
******************************************************************************
Return correct data for the selected model
******************************************************************************
"""


def returnModelData(selectedInput, selectedModel):
    if selectedInput == "era5":
        if selectedModel == "cosmo":
            return cosmo_era5_dic_list, cosmo_era5_infile_list, cosmo_era5_out_file
        else:
            return wrf_era5_dic_list, wrf_era5_infile_list, wrf_era5_out_file
    else:
        if selectedModel == "cosmo":
            return cosmo_interim_dic_list, cosmo_interim_infile_list, cosmo_interim_out_file
        else:
            return wrf_interim_dic_list, wrf_interim_infile_list, wrf_interim_out_file
