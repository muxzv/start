local Player = game:GetService("Players").LocalPlayer
local Char = game.Workspace:WaitForChild(Player.Name)
local Humanoid = Char:WaitForChild("Humanoid")
local RunService = game:GetService("RunService")

RunService.RenderStepped:Connect(function()
	local CT = tick()
	
	if Humanoid.MoveDirection.Magnitude > 0 then
		local BobbleX = math.cos(CT*5)*0.25
		local BobbleY = math.abs(math.sin(CT*5))*0.25
		local Bobble = Vector3.new(BobbleX,BobbleY,0)
		Humanoid.CameraOffset = Humanoid.CameraOffset:lerp(Bobble, 0.25)
	else
		Humanoid.CameraOffset = Humanoid.CameraOffset * 0.75
	end
end)
