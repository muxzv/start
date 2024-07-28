local cam = workspace.CurrentCamera
local RS = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
local Flashlight = RS.Flashlight
local Clone = Flashlight:Clone()
Clone.Parent = script.Parent

local Brightness = 5

local Keybind = Enum.KeyCode.F

local UIS = game:GetService("UserInputService")

local Toggle = false

local Mouse = game.Players.LocalPlayer:GetMouse()

local TS = game:GetService("TweenService")
local TI = TweenInfo.new(.1, Enum.EasingStyle.Sine)


UIS.InputBegan:Connect(function(Input, p)
	if p then return end
	if Input.KeyCode == Keybind then
		Toggle = not Toggle
	end
end)

RunService.RenderStepped:Connect(function()
	if Clone then

		Clone.Position = cam.CFrame.Position
		TS:Create(Clone, TI, {CFrame = CFrame.lookAt(Clone.Position, Mouse.Hit.Position)}):Play()

		if Toggle then
			TS:Create(Clone.SpotLight, TI, {Brightness = Brightness}):Play()

		else
			TS:Create(Clone.SpotLight, TI, {Brightness = 0}):Play()
		end

	end
end)
