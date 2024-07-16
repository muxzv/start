local part = script.Parent
local clicker = part.ClickDetector
local elevator = part.Parent.lift.PrismaticConstraint
local used = false

clicker.MouseClick:Connect(function(player)
	used = not used
	
	print(used)

	if used then
		elevator.TargetPosition = 1
	else
		elevator.TargetPosition = 68
	end
end)
