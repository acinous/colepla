from Course import Course

# Correlate Courses

survey = Course(courseID=1100.15, courseName="Introduction to Ohio State and Engineering", creditHrs=1, dept="Engineering", prerequisites="")
fundOfEngI = Course(courseID=1181, courseName="Fundamentals of Engineering I", creditHrs=2, dept="Engineering", prerequisites="")
fundOfEngII = Course(courseID=1181, courseName="Fundamentals of Engineering II", creditHrs=2, dept="Engineering", prerequisites=[fundOfEngI])
calculusI = Course(courseID=1151, courseName="Calculus I", creditHrs=5, dept="Mathematics", prerequisite="")
physicsI = Course(courseID=1250, courseName="Mechanics, Work and Energy, Thermal Physics", creditHrs=5, dept="Physics", prerequisites=[calculusI])
calculusII = Course(courseID=1152, courseName="Calculus II", creditHrs=5, dept="Mathematics", prerequisites=[calculusI])
calculusIII = Course(courseID=2153, courseName="Calculus III", creditHrs=4, dept="Mathematics", prerequisites=[calculusII])
diffeqns = Course(courseID=2415, courseName="Ordinary and Partial Differential Equations", creditHrs=3, dept="Mathematics", prerequisites=[calculusIII])
linAlg = Course(courseID=2568, courseName="Linear Algebra", creditHrs=3, dept="Mathematics", prerequisites=[calculusIII])
physicsII = Course(courseID=1251, courseName="E&M, Waves, Optics, Modern Physics", creditHrs=5, dept="Physics", prerequisites=[physicsI])
genChemI = Course(courseID=1210, courseName="General Chemistry I", creditHrs=5, dept="Chemistry", prerequisites=[])
engCoding = Course(courseID=1222, courseName="Introduction to Computer Programming in C++ for Engineers and Scientists", creditHrs=3, dept="Computer Science & Engineering", prerequisites=[])
probNStat = Course(courseID=3470, courseName="Introduction to Probability and Statistics for Engineers", creditHrs=3, dept="Statistics", prerequisites=[calculusII])
engEcon = Course (courseID=2040, courseName="Engineering Economics", creditHrs=2, dept="Integrated Systems Engineering", prerequisites=[])
engEthics = Course (courseID=1332, courseName="Ethics in the Professions: Introduction to Engineering Ethics", creditHrs=3, dept="Philosophy", prerequisites=[])


# Major Core Courses

DigitalLogic = Course(courseID=2060, courseName="Introduction to Digital Logic", creditHrs=3, dept="Electrical and Computer Engineering", prerequisites=[])
AnalogSysCirc = Course(courseID=2020, courseName="Introduction to Analog Systems and Circuits", creditHrs=3, dept="Electrical and Computer Engineering", prerequisites=[calculusII, physicsI, fundOfEngII])
DiscreteSignals = Course(courseID=2050, courseName="Introduction to Discrete Time Signals & Systems", creditHrs=3, dept="Electrical and Computer Engineering", prerequisites=[DigitalLogic, engCoding, linAlg])
Microcontrollers = Course(courseID=2560, courseName="Introduction to Microcontroller-Based Systems", creditHrs=2, dept="Electrical and Computer Engineering", prerequisites=[DigitalLogic, engCoding])
RFOptical = Course(courseID=3010, courseName="Introduction to Radio Frequency and Optical Engineering", creditHrs=3, dept="Electrical and Computer Engineering", prerequisites=[AnalogSysCirc, physicsII, diffeqns])
Electronics = Course(courseID=3020, courseName="Introduction to Electronics", creditHrs=3, dept="Electrical and Computer Engineering", prerequisites=[AnalogSysCirc, ElectsLab])
ElectsLab = Course(courseID=3027, courseName="Electronics Laboratory", creditHrs=1, dept="Electrical and Computer Engineering", prerequisites=[Electronics])
Semiconductors = Course(courseID=3030, courseName="Semiconductor Electronic Devices", creditHrs=3, dept="Electrical and Computer Engineering", prerequisites=[physicsII, genChemI, diffeqns])
Energy = Course(courseID=3040, courseName="Sustainable Energy and Power Systems I", creditHrs=3, dept="Electrical and Computer Engineering", prerequisites=[AnalogSysCirc])
SignalsSystems = Course(courseID=3050, courseName="Signals and Systems", creditHrs=3, dept="Electrical and Computer Engineering", prerequisites=[AnalogSysCirc, linAlg])
capstoneI = Course(courseID=3906, courseName="Capstone Design I", creditHrs=4, dept="Electrical and Computer Engineering", prerequisites=[engEthics, Microcontrollers, RFOptical, Electronics, ElectsLab, Semiconductors, Energy, SignalsSystems])
capstoneII = Course(courseID=4905, courseName="Capstone Design II", creditHrs=3, dept="Electrical and Computer Engineering", prerequisites=[capstoneI])