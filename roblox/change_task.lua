local Trigger = workspace.Trigger1
local Wall = workspace.Wall
Wall.CanCollide = false
Wall.Transparency = 1

function Ontouch()
	script.Parent.SubText.Text = "Find a lamp"
	Wall.CanCollide = true
	Wall.Transparency = 0
end
Trigger.Touched:Connect(Ontouch)

--129.3, 0.5, 49


