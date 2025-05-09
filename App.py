from vpython import *
from math import sin, cos, radians, pi
import random

# Configuration
USE_REALISTIC_SCALE = False  # Set to True for realistic scale (makes planets very small)
SHOW_ORBITS = True
SHOW_LABELS = True
ENABLE_TRAILS = False
ENABLE_ROTATION = False  # Enable automatic camera rotation

# Scene setup
scene.width = 1720
scene.height = 920
scene.background = color.black
scene.range = 40
scene.forward = vector(-1, -1, -1)
scene.autoscale = False

# Create buttons and controls
running = True
def toggle_simulation():
    global running
    running = not running
    if running:
        pause_button.text = "Pause"
    else:
        pause_button.text = "Resume"

def toggle_orbits():
    global orbit_visible
    orbit_visible = not orbit_visible
    for orbit in orbit_paths:
        orbit.visible = orbit_visible

def toggle_labels():
    global labels_visible
    labels_visible = not labels_visible
    for label_obj in planet_labels:
        label_obj.visible = labels_visible

def toggle_trails():
    global trails_enabled
    trails_enabled = not trails_enabled
    for planet, _, _ in planets:
        planet.make_trail = trails_enabled

def toggle_rotation():
    global ENABLE_ROTATION
    ENABLE_ROTATION = not ENABLE_ROTATION

def reset_view():
    scene.forward = vector(-1, -1, -1)
    scene.up = vector(0, 1, 0)
    scene.range = 40

# Add a line break
scene.caption = "<br>"

# Create buttons with proper styling
button_width = "180px"
button_margin = "8px"

pause_button = button(text="Pause", bind=toggle_simulation)
pause_button.style = {"height": "30px", "width": button_width, "margin": button_margin, "font-size": "14px"}
scene.append_to_caption(' ')

orbit_button = button(text="Toggle Orbits", bind=toggle_orbits)
orbit_button.style = {"height": "30px", "width": button_width, "margin": button_margin, "font-size": "14px"}
scene.append_to_caption(' ')

label_button = button(text="Toggle Labels", bind=toggle_labels)
label_button.style = {"height": "30px", "width": button_width, "margin": button_margin, "font-size": "14px"}
scene.append_to_caption(' ')

trails_button = button(text="Toggle Trails", bind=toggle_trails)
trails_button.style = {"height": "30px", "width": button_width, "margin": button_margin, "font-size": "14px"}
scene.append_to_caption('<br><br>')

rotation_button = button(text="Toggle Auto-Rotation", bind=toggle_rotation)
rotation_button.style = {"height": "30px", "width": button_width, "margin": button_margin, "font-size": "14px"}
scene.append_to_caption(' ')

reset_button = button(text="Reset View", bind=reset_view)
reset_button.style = {"height": "30px", "width": button_width, "margin": button_margin, "font-size": "14px"}
scene.append_to_caption('<br><br>')

# Initialize variables
orbit_visible = SHOW_ORBITS
labels_visible = SHOW_LABELS
trails_enabled = ENABLE_TRAILS

# Add slider for time speed
scene.append_to_caption('<b>Simulation Speed:</b><br>')
time_speed = 1.0
def update_speed(s):
    global time_speed
    time_speed = s.value
speed_slider = slider(min=0.1, max=5.0, value=1.0, length=400, bind=update_speed)
scene.append_to_caption('<br><br>')

# Add credits with proper styling
scene.append_to_caption('<b>Developed By:</b><br>')
scene.append_to_caption('Gina-Lenn Bejoc<br>')
scene.append_to_caption('Alvan Jay Mayran<br>')
scene.append_to_caption('Cyrus Bon Dimain<br>')
scene.append_to_caption('Ramses Manalo<br><br>')
scene.append_to_caption('<b>BSCS 3A</b><br><br>')

# Add lighting
distant_light(direction=vector(1, 1, 1), color=color.white)
local_light(pos=vector(0,0,0), color=color.yellow)

# Create background stars
num_stars = 300
for _ in range(num_stars):
    sphere(
        pos=vector(random.uniform(-200, 200), random.uniform(-200, 200), random.uniform(-200, 200)),
        radius=0.05 + random.uniform(0, 0.1), 
        color=color.white,
        emissive=True,
        opacity=0.8
    )

if USE_REALISTIC_SCALE:
    # Realistic scale (distances in AU, sizes in Earth radii)
    sun_radius = 109.2  # Sun's radius in Earth radii
    scale_factor = 5    # Scale factor to make planets visible
    planets_data = [
        ("Mercury", 0.39, 0.38, color.gray(0.6), 4.1, 0.03, False, None),
        ("Venus", 0.72, 0.95, color.orange, 1.6, 177.4, False, None),
        ("Earth", 1.00, 1.00, color.blue, 1.0, 23.4, False, None),
        ("Mars", 1.52, 0.53, color.red, 0.53, 25.2, False, None),
        ("Jupiter", 5.20, 11.2, color.orange, 0.084, 3.1, False, None),
        ("Saturn", 9.58, 9.45, color.yellow, 0.034, 26.7, True, {"inner": 1.5, "outer": 2.3, "color": color.white}),
        ("Uranus", 19.22, 4.01, color.cyan, 0.012, 97.8, True, {"inner": 1.3, "outer": 1.7, "color": color.gray(0.8)}),
        ("Neptune", 30.05, 3.88, color.blue, 0.006, 28.3, False, None)
    ]
else:
    # Visual scale for better viewing
    sun_radius = 2.5
    scale_factor = 1
    planets_data = [
        ("Mercury", 4, 0.2, color.gray(0.6), 1.6, 0.03, False, None),
        ("Venus", 6, 0.4, color.orange, 1.2, 177.4, False, None),
        ("Earth", 8, 0.5, color.blue, 1.0, 23.4, False, None),
        ("Mars", 10, 0.3, color.red, 0.8, 25.2, False, None),
        ("Jupiter", 14, 1.1, color.orange, 0.4, 3.1, False, None),
        ("Saturn", 18, 0.9, color.yellow, 0.3, 26.7, True, {"inner": 1.2, "outer": 2.0, "color": color.white}),
        ("Uranus", 22, 0.7, color.cyan, 0.2, 97.8, True, {"inner": 1.1, "outer": 2.5, "color": color.gray(0.8)}),
        ("Neptune", 26, 0.7, color.blue, 0.1, 28.3, False, None)
    ]

sun = sphere(
    pos=vector(0,0,0), 
    radius=sun_radius, 
    color=color.yellow, 
    emissive=True,
    shininess=0,  # Reduce shininess to make the texture brighter
    opacity=1.0,
    texture={
        "file": textures.stucco,
        "bumpmap": textures.stucco
    }
)

# Add a glowing effect around the sun
glow = sphere(
    pos=vector(0,0,0),
    radius=sun_radius * 1.1,
    color=color.yellow,
    opacity=0.2,
    emissive=True
)

# Create planets and their orbits
planets = []
orbit_paths = []
planet_labels = []
angles = {}
planet_info = {}  # Store additional info about planets

# Create planets
for name, dist, rad, col, speed, tilt, has_rings, ring_details in planets_data:
    # Create orbit path
    if SHOW_ORBITS:
        orbit = curve(color=color.gray(0.5), radius=0.01)
        for angle in range(0, 361, 10):  # Create points along orbit
            angle_rad = radians(angle)
            orbit.append(vector(dist * cos(angle_rad), 0, dist * sin(angle_rad)))
        orbit_paths.append(orbit)
    
    # Create planet
    p = sphere(
        pos=vector(dist, 0, 0), 
        radius=rad * scale_factor, 
        color=col, 
        make_trail=ENABLE_TRAILS, 
        trail_type="curve", 
        interval=10,
        retain=100,
        texture=textures.stucco  # Add a basic texture
    )
    
    # Create label
    lbl = label(
        pos=p.pos, 
        text=name, 
        xoffset=20,
        yoffset=20, 
        space=30, 
        height=10, 
        color=color.white,
        visible=SHOW_LABELS
    )
    planet_labels.append(lbl)
    
    # Add to planet list
    planets.append((p, dist, speed))
    angles[name] = random.uniform(0, 360)  # Random starting position
    
    # Add rings if applicable
    if has_rings and ring_details:
        inner_radius = rad * scale_factor * ring_details["inner"]
        outer_radius = rad * scale_factor * ring_details["outer"]
        ring_color = ring_details["color"]

        # Create realistic rings using multiple concentric curves
        num_rings = 8  # Number of concentric rings (reduced for performance)
        rings = []
        ring_thickness = (outer_radius - inner_radius) / num_rings
        for i in range(num_rings):
            ring_radius = inner_radius + i * ring_thickness
            opacity = 0.7 - (i / num_rings) * 0.5  # Gradually fade the opacity
            ring = curve(
                pos=[p.pos + vector(ring_radius * cos(radians(angle)), 0, ring_radius * sin(radians(angle))) for angle in range(0, 361, 10)],
                radius=0.01,
                color=ring_color,
                opacity=opacity
            )
            rings.append(ring)
        
        # Store the rings with the planet
        planet_info[name] = {"planet": p, "rings": rings}
    else:
        planet_info[name] = {"planet": p}

# Earth's moon
moon = sphere(
    pos=vector(planets_data[2][1] + 0.7, 0, 0),  # Earth's distance + moon distance
    radius=0.1 * scale_factor, 
    color=color.white, 
    make_trail=False,
    texture=textures.stucco
)
moon_angle = 0
moon_speed = 7
moon_distance = 0.7

# Create multiple meteors (shooting stars)
meteors = []
for _ in range(3):  # Create 3 meteors
    meteor = sphere(
        pos=vector(
            random.uniform(-50, -30), 
            random.uniform(-10, 10), 
            random.uniform(-10, 10)
        ),
        radius=0.15,
        color=color.white,
        make_trail=True,
        trail_type="curve",
        retain=30,
        emissive=True
    )
    velocity = vector(
        random.uniform(1.0, 2.0),
        random.uniform(-0.2, 0.2),
        random.uniform(-0.2, 0.2)
    )
    meteors.append((meteor, velocity))

# Camera rotation settings
rotation_angle = 0
rotation_speed = 0.05

# Planet info display
info_label = label(pos=scene.center, text="", visible=False, height=15, color=color.white)

# Function to display information when clicking on a planet
def handle_click(event):
    global info_label
    
    # Reset any previous info
    info_label.visible = False
    
    # Get the object that was clicked
    obj = scene.mouse.pick
    
    if obj:
        # Check if it's the sun
        if obj == sun:
            info_text = "Sun\nThe center of our solar system\nDiameter: 1,391,000 km\nSurface Temperature: 5,500°C"
            info_label.text = info_text
            info_label.pos = sun.pos + vector(0, sun.radius + 1, 0)
            info_label.visible = True
            return
            
        # Check if it's a planet
        for name, data in planet_info.items():
            if obj == data["planet"]:
                planet_data = next((p for p in planets_data if p[0] == name), None)
                if planet_data:
                    info_text = f"{name}\nDistance from Sun: {planet_data[1]} units\nDiameter: {planet_data[2]*2} units\nOrbital Period: {1/planet_data[4]:.2f} Earth years"
                    info_label.text = info_text
                    info_label.pos = obj.pos + vector(0, obj.radius + 1, 0)
                    info_label.visible = True
                    return

scene.bind('click', handle_click)

# Simulation loop
t = 0
while True:
    rate(60)
    
    # Only update if simulation is running
    if running:
        t += time_speed * 0.01
        
        # Update planets
        for idx, (planet, dist, speed) in enumerate(planets):
            name = planets_data[idx][0]
            angles[name] += speed * time_speed
            rad = radians(angles[name])
            
            planet.pos = vector(dist * cos(rad), 0, dist * sin(rad))
            
            # Update planet label
            planet_labels[idx].pos = planet.pos
            
            # Update rings if the planet has them
            if name in planet_info and "rings" in planet_info[name]:
                rings = planet_info[name]["rings"]
                for i, ring in enumerate(rings):
                    inner_radius = planet_info[name]["planet"].radius * (ring_details["inner"] if has_rings and ring_details else 1.5)
                    outer_radius = planet_info[name]["planet"].radius * (ring_details["outer"] if has_rings and ring_details else 2.0)
                    ring_thickness = (outer_radius - inner_radius) / len(rings)
                    ring_radius = inner_radius + i * ring_thickness
                    
                    # Update ring position
                    new_ring_pos = []
                    for angle in range(0, 361, 10):
                        angle_rad = radians(angle)
                        new_ring_pos.append(planet.pos + vector(ring_radius * cos(angle_rad), 0, ring_radius * sin(angle_rad)))
                    
                    ring.clear()
                    for pos in new_ring_pos:
                        ring.append(pos)
    
        # Update moon position (orbiting Earth)
        moon_angle += moon_speed * time_speed
        moon_rad = radians(moon_angle)
        earth_pos = planets[2][0].pos  # Earth's position
        moon.pos = earth_pos + vector(moon_distance * cos(moon_rad), 0, moon_distance * sin(moon_rad))
    
        # Move meteors
        for meteor, velocity in meteors:
            meteor.pos = meteor.pos + velocity * time_speed
            
            # If meteor leaves the view, reset its position and trail
            if meteor.pos.x > 50:
                meteor.clear_trail()
                meteor.pos = vector(
                    random.uniform(-50, -30), 
                    random.uniform(-10, 10), 
                    random.uniform(-10, 10)
                )
        
        # Update camera position for rotation
        if ENABLE_ROTATION:
            rotation_angle += rotation_speed * time_speed
            scene.camera.pos = vector(40 * sin(rotation_angle), 15, 40 * cos(rotation_angle))
            scene.camera.axis = scene.center - scene.camera.pos
    
    # Update info label position if visible
    if info_label.visible:
        # Find the object the label is attached to
        for name, data in planet_info.items():
            if info_label.pos.mag - data["planet"].pos.mag < 5:  # Rough check if label is near this planet
                info_label.pos = data["planet"].pos + vector(0, data["planet"].radius + 1, 0)
                break