[![Markdown Acronym Workflow](https://github.com/sfrinaldi/acronyms-test/actions/workflows/md-workflow.yml/badge.svg)](https://github.com/sfrinaldi/acronyms-test/actions/workflows/md-workflow.yml)

# UASAL / Acronyms
For storing the latest versions of acronyms for other repos to pull from. The [`combined_acronyms.tex`](combined_acronyms.tex) file was generating by using non-duplicate values from original .tex files found in other repos and on Overleaf. These can be viewed in the [archives](archives/) directory. The purpose of having one acronym.tex file instead of multiple is to limit issues with compiling latex documentation if there are duplicate listings. A rough script for generating a markdown file from the combined .tex acronyms file provided as well.

## Editing Information
- Apply updates to the [`combined_acronyms.tex`](combined_acronyms.tex) file. 
- Update `Modified` section in [`combined_acronyms.tex`](combined_acronyms.tex) with the date you edited the file.
- **VERIFY** added acronyms are not already within the dictionary as this will cause issues in latex generating repositories that use this repo for acronym pulling.
  - Eventually, a check can be added to this repo for doing automatically. 
- GitHub workflow will update this README.md files' markdown conversion run display and add a new [`combined-acronyms.md`](combined-acronyms.md) file with the adjustments.
  - This format can be changed to a markdown table if of use in the future.

**Results of the last latex to markdown conversion run shown below:**

---------------------------------
# Acronym Listing / Descriptions
- Working list of active and past acronyms / abbreviations used for a variety of projects.
- Refer to the acronyms.tex file for making additional edits and updates to this sheet.

## Edit Notes & Information:
- Modified- 20240125 (YYYYMMDD)
- Notes: Combined other acronym listings to this file and added some missing acronyms.

---------------------------------

## Units:

- AU -> AU -> astronomical Unit [1.5e11 m]
- pc -> pc -> parsec
- mas -> mas -> milliarcsecond
- nm -> nm -> nanometer
- CTE -> CTE -> coefficient of thermal expansion
- sqarc -> as^2 -> square arcsecond
- ppm -> ppm -> Part Per Million

---------------------------------

## Astrophysics:

- smc -> SMC -> Small Magellanic Cloud
- lmc -> LMC -> Large Magellanic Cloud
- ism -> ISM -> interstellar medium
- mw -> MW -> Milky Way
- epseri -> $\epsilon$ Eri -> Epsilon Eridani
- EKB -> EKB -> Edgeworth-Kuiper Belt
- CFR -> CFR -> Complete Frequency Redistribution

---------------------------------

## Organizations:

- nasa -> NASA -> National Aeronautics and Space Agency
- esa -> ESA -> European Space Agency
- omi -> OMI -> *Optical Mechanics Inc.
- gsfc -> GSFC-> Lower-Case: nasa -> Goddard Space Flight Center
- stsci -> STScI -> Space Telescope Science Institute
- nsroc -> NSROC-> Lower-Case: nasa -> Sounding Rocket Operations Contract
- wff -> WFF-> Lower-Case: nasa -> Wallops Flight Facility
- wsmr -> WSMR -> White Sands Missile Range
- BCT -> BCT -> Blue Canyon Technologies
- SFL -> SFL -> Spaceflight Laboratory
- UA -> UA -> University of Arizona
- UTIAS -> UTIAS -> University of Toronto Institute for Aerospace Studies
- DIATF -> DIATF -> Drake Imager Assembly and Testing Facility
- ETS -> ets -> Engineering Technical Services
- ASTM -> ASTM -> American Society for Testing and Materials

---------------------------------

## Technologies and Sensors:

- irac -> IRAC -> Infrared Array Camera
- Plural= CCDs, charge-coupled devices (CCDs) -> ccd -> CCD -> charge-coupled device
- Plural= EMCCDs, electron multiplying charge-coupled devices (EMCCDs) -> EMCCD -> EMCCD -> electron multiplying charge-coupled device
- DM -> DM -> Deformable Mirror
- ipc -> IPC -> Image Proportional Counter
- cots -> COTS -> Commercial Off-The-Shelf
- COTS -> COTS -> commercial off-the-shelf
- ISR -> ISR -> incoherent scatter radar
- atcamera -> AT -> angle tracker
- MEMS -> MEMS -> microelectromechanical systems
- QE -> QE -> quantum efficiency
- RTD -> RTD -> Resistance Temperature Detector
- PID -> PID -> Proportional-Integral-Derivative
- PRNU -> PRNU -> photo response non-uniformity
- DSNU -> PRNU -> dark signal non-uniformity
- CMOS -> CMOS -> complementary metal–oxide–semiconductor
- TEC -> TEC -> thermoelectric cooler

---------------------------------

## Optics:

- FOV -> FOV -> field-of-view
- NIR -> NIR -> near-infrared
- PV -> PV -> Peak-to-Valley
- MRF -> MRF -> Magnetorheological finishing
- AO -> AO -> Adaptive Optics
- TTP -> TTP -> tip, tilt, and piston
- FPS -> FPS -> fine pointing system
- SHWFS -> SHWFS -> Shack-Hartmann Wavefront Sensor
- OAP -> OAP -> off-axis parabola
- LGS -> LGS -> laser guide star
- WFCS -> WFCS -> wavefront control system
- OPD -> OPD -> optical path difference
- MEL -> MEL -> Master Equipment List
- EFC -> EFC -> electric-field conjugation
- iEFC -> EFC -> implicit -> Lower-Case= EFC
- LDFC -> LDFC -> linear dark field control
- DAC -> DAC -> digital-to-analog converter
- TMA -> TMA -> three-mirror anastigmat
- resel -> resel -> resolution element
- BOM -> BOM -> Bill of Materials

---------------------------------

## Spacecraft and Sounding Rocket:

- acs -> ACS -> attitude control system
- orsa -> ORSA -> Ogive Recovery System Assembly
- gse -> GSE -> ground station equipment
- FSM -> FSM -> fast steering Mirror
- CFRP -> CRFP -> carbon fiber reinforced plastic
- CDP -> CDP -> critical design phase
- CDR -> CDR -> critical design review
- LEO -> LEO -> low-earth orbit
- GEO -> GEO -> geosynchronous orbit
- FEA -> FEA -> finite element analysis
- ESPA -> ESPA -> EELV Secondary Payload Adapter
- EEID -> EEID -> Earth-equivalent Insolation Distance, the distance from the star where the incident energy density is that of the Earth received from the Sun
- STOP -> STOP -> Structural-Thermal-Optical-Performance
- STM -> STM -> science traceability matrix
- ConOps -> ConOps -> concept of operations
- NRE -> NRE -> non-recurring engineering
- CSR -> CSR -> concept study report
- XAO -> XAO -> extreme-adaptive optics
- AT -> AT -> angle tracking camera
- SRR -> SRR -> system requirements review
- ROI -> ROI -> region of interest
- LCP -> LCP -> liquid-crystal polymer
- CBE -> CBE -> current best estimate
- SBC -> SBC -> single-board computer
- ADCS -> ADCS -> attitude determination and control system
- CDH -> C&DH -> command and data handling
- EPS -> EPS -> electrical power system
- TLE -> TLE -> Two Line Element set
- TRL -> TRL -> technology readiness level
- swap -> SWaP -> Size, Weight, and Power

---------------------------------

## High Contrast Imaging:

- WFS -> WFS -> wavefront sensor
- LSI -> LSI -> Lateral Shearing Interferometer
- VVC -> VVC -> Vector Vortex Coronagraph
- VNC -> VNC -> Visible Nulling Coronagraph
- CGI -> CGI -> Coronagraph Instrument
- IWA -> IWA -> Inner Working Angle
- OWA -> OWA -> Outer Working Angle
- NPZT -> N-PZT -> Nuller piezoelectric transducer
- ZWFS -> ZWFS -> Zernike wavefront sensor
- SPC -> SPC -> Shaped Pupil Coronagraph
- HLC -> HLC -> Hybrid-Lyot Coronagraph
- ADI -> ADI -> angular differential imaging
- RDI -> RDI -> reference differential imaging
- HOWFSC -> HOWFS/C -> high-order wavefront sensing and control
- WFSC -> WFSC -> wavefront sensing and control
- CDI -> CDI -> coherent differential imaging
- SCC -> SCC -> self-coherent camera
- LLOWFS -> LLOWFS -> Lyot low-order wavefront sensor
- VSG -> VSG -> vacuum surface gauge
- TDEM -> TDEM -> Technology Development for Exoplanet Missions
- HZ -> HZ -> habitable zone
- ODI -> ODI -> orbital-differential imaging
- PSFTFC -> PSFTFC -> PSF template subtracted coronagraphy
- LOWFSC -> LOWFSC -> Low-order -> Lower-Case= WFS -> and control
- scoob -> SCoOB -> Space Coronagraph Optical Bench
- FDPR -> FDPR -> focus diversity phase retrieval

---------------------------------

## Observatories and Instruments:

- HST -> HST -> Hubble Space Telescope
- GPS -> GPS -> Global Positioning System
- ISS -> ISS -> International Space Station
- Description= Advanced CCD Imaging Spectrometer -> acis -> ACIS -> Advanced -> Lower-Case= ccd -> Imaging Spectrometer
- stis -> STIS -> *Space Telescope Imaging Spectrograph
- mcp -> MCP -> Microchannel Plate
- jwst -> JWST -> *JWST
- fuse -> FUSE -> *FUSE
- galex -> GALEX -> *Galaxy Evolution Explorer
- spitzer -> Spitzer -> *Spitzer Space Telescope
- mips -> MIPS -> Multiband Imaging Photometer for -> Lower-Case= spitzer
- gissmo -> GISSMO -> Gas Ionization Solar Spectral Monitor
- iue -> IUE -> International Ultraviolet Explorer
- spinr -> SPINR -> *Spectrograph for Photometric Imaging with Numeric Reconstruction
- imager -> IMAGER -> *Interstellar Medium Absorption Gradient Experiment Rocket
- TPF-C -> TPF-C -> Terrestrial Planet Finder Coronagraph
- RAIDS -> RAIDS -> Atmospheric and Ionospheric Detection System 
- mama -> MAMA -> Multi-Anode Microchannel Array
- ATLAST -> ATLAST -> Advanced Technology Large Aperture Space Telescope
- PICTURE -> PICTURE -> Planet Imaging Concept Testbed Using a Rocket Experiment
- LITES -> LITES -> Limb-imaging Ionospheric and Thermospheric Extreme-ultraviolet Spectrograph
- LBT -> LBT -> Large Binocular Telescope
- LBTI -> LBTI -> Large Binocular Telescope Interferometer
- KIN -> KIN -> Keck Interferometer Nuller
- SHARPI -> SHARPI -> Solar High-Angular Resolution Photometric Imager
- IRAS -> IRAS -> Infrared Astronomical Satellite
- HARPS -> HARPS -> High Accuracy Radial velocity Planetary
- hstSTIS -> STIS -> Space Telescope Imaging Spectrograph
- spitzerIRAC -> IRAC -> Infrared Array Camera
- spitzerMIPS -> MIPS -> Multiband Imaging Photometer for Spitzer
- spitzerIRS -> IRS -> Infrared Spectrograph
- CHARA -> CHARA -> Center for High Angular Resolution Astronomy
- wfirst-afta -> WFIRST-AFTA -> Wide-Field InfrarRed Survey Telescope-Astrophysics Focused Telescope Assets
- GPI -> GPI -> Gemini Planet Imager
- WFIRST -> Roman -> Nancy Grace Roman Space Telescope
- HabEx -> HabEx -> Habitable Exoplanet Observatory Mission Concept
- FGS -> FGS -> Fine Guidance Sensor
- MGHPCC -> MGHPCC -> Massachusetts Green High Performance Computing Center
- WISE -> WISE -> Wide-field Infrared Survey Explorer
- ALMA -> ALMA -> Atacama Large Millimeter Array
- GRAIL -> GRAIL -> Gravity Recovery and Interior Laboratory
- jwstNIRCam -> NIRCam -> near--> Lower-Case= IR-camera
- jwstMIRI -> MIRI -> Mid-Infrared Instrument
- LUVOIR -> LUVOIR -> Large UV Optical IR Surveyor
- Roman -> Roman -> Nancy Grace Roman Space Telescope
- STP -> HLST -> Hypothetical Large Space Telescopes
- CDEEP -> ESC -> STP ExtraSolar Camera, a Coronagraphic Pathfinder
- ESC -> ESC -> ExtraSolar Camera
- CCS -> WCC -> Wavefront and Context Camera
- WCC -> WCC -> Wavefront and Context Camera
- LSST -> LSST -> Large Synoptic Survey Telescope
- M1 -> M1 -> Mirror 1 (Telescope Module Primary Mirror)
- M2 -> M2 -> Mirror 2 (Telescope Module Secondary Mirror)
- M3 -> M3 -> Mirror 3
- M4 -> M4 -> Mirror 4
- AOA -> AOA -> Aft-Optics Assembly
- FOA -> FOA -> Fore-Optics Assembly
- AOSS -> AOSS -> Aft-optics Support Structure
- MMTO -> MMTO -> MMT Observatory
- MMT -> MMT -> Multiple Mirror Telescope
- PMCC -> PMCC -> primary mirror (M1) control computer
- PMSS -> PMSS -> primary mirror (M1) support structure
- UASAL -> UASAL -> UArizona Space Astrophysics Lab
- ITL -> ITL -> Imaging Technology Lab
- TAO -> TAO -> Tokyo Atacama Observatory
- UVS -> UVS -> Ultraviolet Spectrograph
- IFS -> IFS -> Integral Field Spectrograph
- STIS -> STIS -> Space Telescope Imaging Spectrograph
- SCoOB -> scoob -> space-coronagraph optical bench

---------------------------------

## Software:

- AURIC -> AURIC -> The Atmospheric Ultraviolet Radiance Integrated Code
- FFT -> FFT -> Fast Fourier Transform  
- MODTRAN -> MODTRAN    ->  MODerate resolution atmospheric TRANsmission 
- idl -> IDL -> *Interactive Data Language
- sort=NED,Description= NASA/IPAC Extragalactic Database -> ned -> NED-> Lower-Case: nasa/-> Lower-Case= ipac -> Extragalactic Database
- iraf -> IRAF -> Image Reduction and Analysis Facility
- wcs -> WCS -> World Coordinate System
- pegase -> PEGASE -> *Projet d'Etude des GAlaxies par Synthese Evolutive
- dirty -> DIRTY -> *DustI Radiative Transfer, Yeah!
- CUDA -> CUDA -> Compute Unified Device Architecture
- KLIP -> KLIP -> Karhunen-Lo`eve Image Processing
- FEM -> FEM -> finite element method
- CLI -> CLI -> command-line interface
- CAD -> CAD -> computer-aided design
- DBMS -> DBMS -> database management system
- POPPY -> POPPY -> Physical Optics Propagation in Python
- SOEDMS -> SOEDMS -> Steward Observatory Electronic Data Management System

---------------------------------

## Earth's Atmosphere and Ionosphere:

- MSIS -> MSIS -> Mass Spectrometer Incoherent Scatter Radar
- nmf2 -> N_m -> F2-Region Peak density
- hmf2 -> h_m -> F2-Region Peak height
- H -> H -> F2-Region Scale Height

---------------------------------

## Misc jargon:

- isr -> ISR -> Incoherent Scatter Radar
- Description= TLA Within Another Acronym -> twaa -> TWAA-> Lower-Case: tla -> Within Another Acronym
- Plural= SNe, Supernovae (SNe) -> sn -> SN -> Supernova
- EUV -> EUV -> Extreme-Ultraviolet
- EUVS -> EUVS-> Lower-Case: EUV -> Spectrograph
- F2 -> F2 -> Ionospheric Chapman F Layer
- F10.7 -> F10.7 ->  10.7 cm radio flux [10^-22 W m^-2 Hz^-1]  
- FUV -> FUV -> far-ultraviolet
- IR -> IR -> infrared
- MUV -> MUV -> mid-ultraviolet 
- NUV -> NUV -> near-ultraviolet
- nir -> NIR -> near-infrared
- mir -> MIR -> mid-infrared
- UV -> UV -> ultraviolet
- O^+ -> O^+ -> Singly Ionized Oxygen  Atom
- OI -> OI -> Neutral Atomic Oxygen Spectroscopic State
- OII -> OII -> Singly Ionized Atomic Oxygen Spectroscopic State
- PSF -> PSF -> point spread function
- R_E -> R_E -> Earth radii [~ 6400 km] 
- RV -> RV -> radial velocity
- WFE -> WFE -> wavefront error
- sed -> SED -> spectral energy distribution
- Plural= PAHs, Polycyclic Aromatic Hydrocarbons (PAHs) -> pah -> PAH -> Polycyclic Aromatic Hydrocarbon
- obsid -> OBSID -> Observation Identification
- SZA -> SZA -> Solar Zenith Angle
- PZT -> PZT -> lead zirconate titanate
- AIT -> AIT -> Assembly, Integration and Test
- CPR -> CPR -> cost performance report
- FDR -> FDR -> final design review
- DHS -> DHS -> data handling system
- CNS -> CNS -> communications and network system
- FOC -> FOC -> fiber optic cable
- CDS -> CDS -> correlated double sampling
- DDCP -> DDCP -> document and drawing control plan
- FOCS -> FOCS -> feed optics control system
- CSH -> CSH -> camera systems hardware
- CSS -> CSS -> camera systems software
- DMA -> DMA -> dynamic mechincal anlysis
- MWIR -> MWIR -> midwave infrared
- LWIR -> LWIR -> longwave infrared
- SVD -> SVD -> singular value decomposition
- NRM -> NRM -> normal response mode
- KISS -> KISS -> keep it sans spectrometer
- CIDL -> CIDL -> configuration item data list
- ICD -> ICD -> interface control document
- ERD -> ERD -> Environmental Requirements Document
- EP -> EP -> Telescope Entrance Pupil
- HFOV -> HFOV -> Half Field of View
- L3 -> L3 -> Telescope Module Collimating Lens
- QKD -> QKD -> Quantum Key Distribution
- XP -> XP -> Telescope Exit Pupil
- TBC -> TBC -> To Be Confirmed
- TBD -> TBD -> To Be Determined
- TBR -> TBR -> To Be Reviewed
- EEIS -> EEIS -> End-to-End Information Systems
- EA -> EA -> Executing Agent
- SPGD -> SPGD -> Stochastic Parallel Gradient Descent
- TAM -> TAM -> Test Allocation Matrix
- CCP -> CCP -> Contamination Control Plan
- VC -> VC -> Visualy Clean
- VC-S -> VC-S -> Visualy Clean Sensitive
- VC-HS -> VC-HS -> Visualy Clean High Sensitive
- PAC -> PAC -> Percent Area Coverage
- ATLO -> ATLO -> Assembly Test, and Launch Operations
- QA -> QA -> Quality Assurance
- UUT -> UUT -> Unit Under Test
- P/N -> P/N -> Part Number
- ESD -> ESD -> Electro-static Discharge
- AC -> AC -> Alternating Current
- RH -> RH -> Relative Humidity
- RGA -> RGA -> Residual Gas Analyzer
- esds -> ESDS -> ESD Sensitive
- dmm -> DMM -> Digital Multimeter
- DC -> DC -> Direct Current
- CPG -> CPG -> Common Point Ground
- WM -> WM -> Workmanship Manual
- N/A -> N/A -> Not Applicable
- na -> NA -> Not Applicable
- MM -> MM -> Machine Model [for electrostatic discharge]
- LVDS -> LVDS -> Low-Voltage Differential Signal
- LNA -> LNA -> Low Noise Amplifier


---------------------------------

## Material Abbreviations

- PVC -> PVC -> Polyvinyl Chloride
- PTFE -> PTFE -> Polytetrafluoroethylene (Teflon)

---------------------------------

## Statistics:

- PCA -> PCA -> principal component analysis
- fwhm -> FWHM -> full-width-half maximum
- RMS -> RMS -> root mean squared
- RMSE -> RMSE -> root mean squared error
- MCMC -> MCMC -> Marcov chain Monte Carlo
- DIT -> DIT -> discrete inverse theory
- SNR -> SNR -> signal-to-noise ratio
- PSD -> PSD -> power spectral density
- NMF -> NMF -> non-negative matrix factorization
- DOF -> DOF -> degrees-of-freedom


