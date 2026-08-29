from astropy import units as u
from hapsira.bodies import Earth, Mars, Sun
from hapsira.twobody import Orbit

### Plotting using position and velocity vectors

r = [-6045, -3490, 2500] << u.km            # position vector in km
v = [-3.457, 6.618, 2.533] << u.km / u.s    # velocity vector in km/s

orb = Orbit.from_vectors(Earth, r, v)       # create an orbit from position and velocity vectors
print(orb)                                  # print the orbital elements in r. peri, r. apo, inc, ref frame, epoch
print(orb.epoch.iso)                        # print the epoch in ISO format
orb.plot()

### Plotting Mars' orbit using orbital elements

a = 1.523679 << u.au                        # semi-major axis in AU
e = 0.093315 << u.one                       # eccentricity
inc = 1.85 << u.deg                         # inclination in degrees
raan = 49.562 << u.deg                      # right ascension of ascending node in degrees
argp = 286.537 << u.deg                     # argument of periapsis in degrees
nu = 23.33 << u.deg                         # true anomaly in degrees

orb2 = Orbit.from_classical(Sun, a, e, inc, raan, argp, nu)     # create an orbit from classical orbital elements
print(orb2)                                                     # print the orbital elements in r. peri, r. apo
orb2.plot()                                                     