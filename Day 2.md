# Day 2   
  
  
🔥 Excellent, Shifin.  
Day 1 completed means you officially started your startup journey.  
  
Now we move to:  
  
🚀** DAY 2 MISSION**  
  
🎯** Goal:**  
  
Understand **Objects deeply** + Build multiple electrical components as classes.  
  
Today we move from 1 motor → small system.  
  
⸻  
  
🧠** PART 1 (45 mins) – Improve OOP Thinking**  
  
You must clearly understand:  
	•	Each component has:  
	•	Name  
	•	Terminals  
	•	State  
	•	Each component can:  
	•	Change state  
	•	Report state  
  
Now think like this:  
  
Contactor:  
	•	Coil state (ON/OFF)  
	•	Main contacts (open/closed)  
  
Overload Relay:  
	•	Tripped / Not tripped  
  
Push Button:  
	•	NO or NC  
	•	Pressed or not  
  
⸻  
  
💻** PART 2 (1 hour) – Write This Code Yourself**  
  
Do NOT copy blindly. Type it fully.  
  
  
class Contactor:  
    def __init__(self, name):  
        self.name = name  
        self.coil_energized = False  
  
    def energize(self):  
        self.coil_energized = True  
        print(self.name, "coil energized")  
  
    def deenergize(self):  
        self.coil_energized = False  
        print(self.name, "coil de-energized")  
  
  
class OverloadRelay:  
    def __init__(self, name):  
        self.name = name  
        self.tripped = False  
  
    def trip(self):  
        self.tripped = True  
        print(self.name, "TRIPPED!")  
  
    def reset(self):  
        self.tripped = False  
        print(self.name, "reset")  
  
  
# Testing  
c1 = Contactor("Main Contactor")  
o1 = OverloadRelay("OLR-1")  
  
c1.energize()  
o1.trip()  
  
  
Understand:  
You are creating digital versions of real components.  
  
⸻  
  
🧠** PART 3 (15 mins) – Think Bigger**  
🧠** PART 3 (15 mins) – Think Bigger**  
  
Ask yourself:  
  
In real life:  
If overload trips → contactor should de-energize.  
  
So tomorrow we will connect components logically.  
  
That is how PLC simulation will start.  
  
⸻  
  
🎯** End of Day 2 Checklist**  
🎯** End of Day 2 Checklist**  
  
Before finishing today:  
  
✔ Can you create multiple objects?  
✔ Can you change their state?  
✔ Do you understand how this relates to automation?  
  
⸻  
  
🔥** Important**  
  
You are slowly building the brain of your future software.  
  
Most people stop after 3 days.  
  
You will not.  
  
⸻  
  
When finished, come back and say:  
  
“Day 2 completed.”  
  
Then Day 3 we start building **interaction between components** ⚙🚀  
