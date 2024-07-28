--[[ Made by coolcapidog
Channel ->> https://www.youtube.com/c/coolcapidog
You can change the settings but you shouldn't change anything except settings.
]]

local KeyCode = Enum.KeyCode.E
local HoverAnimID = "rbxassetid://18694713432"
local FlyAnimID = "rbxassetid://18694711393"
local WindSoundEnabled = true

local BodyVelocity = script:WaitForChild("BodyVelocity"):Clone()
local v3 = script.BodyGyro:Clone()
local Character = script.Parent
local Humanoid = Character:FindFirstChild("Humanoid") or Character:WaitForChild("Humanoid")
BodyVelocity.Parent = Character
v3.Parent = Character
local Hover = Instance.new("Animation")
Hover.AnimationId = HoverAnimID
local Fly = Instance.new("Animation")
Fly.AnimationId = FlyAnimID
local Sound1 = Instance.new("Sound", Character.HumanoidRootPart)
Sound1.SoundId = "rbxassetid://3308152153"
Sound1.Name = "Sound1"
if WindSoundEnabled == false then
	Sound1.Volume = 0
end
local v10 = Humanoid.Animator:LoadAnimation(Hover)
local v11 = Humanoid.Animator:LoadAnimation(Fly)
local Camera = game.Workspace.Camera
local function u2()
	if Humanoid.MoveDirection == Vector3.new(0, 0, 0) then
		return Humanoid.MoveDirection
	end
	local v12 = (Camera.CFrame * CFrame.new((CFrame.new(Camera.CFrame.p, Camera.CFrame.p + Vector3.new(Camera.CFrame.lookVector.x, 0, Camera.CFrame.lookVector.z)):VectorToObjectSpace(Humanoid.MoveDirection)))).p - Camera.CFrame.p;
	if v12 == Vector3.new() then
		return v12
	end
	return v12.unit
end
local Flymoving = script.Flymoving
local TweenService = game:GetService("TweenService")
local UIS = game:GetService("UserInputService")
local Flying = false

game:GetService("RunService").RenderStepped:Connect(function()
	if script.Parent == Character then
		if Flying == true then
			Humanoid:ChangeState(6)
			v3.CFrame = game.Workspace.Camera.CFrame
			if u2() == Vector3.new(0, 0, 0) then
				Flymoving.Value = false
			else
				Flymoving.Value = true
			end
			TweenService:Create(BodyVelocity, TweenInfo.new(0.3), {Velocity = u2() * 350}):Play()
		end
		
	end
end)

Flymoving.Changed:Connect(function(p1)
	if p1 == true then
		TweenService:Create(Camera, TweenInfo.new(0.5), {FieldOfView = 100}):Play()
		v10:Stop()
		Sound1:Play()
		v11:Play()
		return
	end
	if p1 == false then
		TweenService:Create(Camera, TweenInfo.new(0.5), {FieldOfView = 70}):Play()
		v11:Stop()
		Sound1:Stop()
		v10:Play()
	end
end)

local xractivated = false

UIS.InputBegan:Connect(function(key, gameProcessed)
	if gameProcessed then return end
	if key.KeyCode == KeyCode then
		if Flying == false then
			Flying = true
			if Character:FindFirstChild("HumanoidRootPart") then
				v10:Play(0.1, 1, 1)
				Humanoid:SetStateEnabled(Enum.HumanoidStateType.Running, false)
				Humanoid:SetStateEnabled(Enum.HumanoidStateType.Climbing, false)
				Humanoid:SetStateEnabled(Enum.HumanoidStateType.FallingDown, false)
				Humanoid:SetStateEnabled(Enum.HumanoidStateType.Freefall, false)
				Character.HumanoidRootPart.Running.Volume = 0
				Humanoid:ChangeState(6)
				BodyVelocity.Parent = Character.HumanoidRootPart
				v3.Parent = Character.HumanoidRootPart
			end
		else
			Flying = false
			Flymoving.Value = false
			Humanoid:SetStateEnabled(Enum.HumanoidStateType.Running, true)
			Humanoid:SetStateEnabled(Enum.HumanoidStateType.Climbing, true)
			Humanoid:SetStateEnabled(Enum.HumanoidStateType.FallingDown, true)
			Humanoid:SetStateEnabled(Enum.HumanoidStateType.Freefall, true)
			Character.HumanoidRootPart.Running.Volume = 0.65
			Humanoid:ChangeState(8)
			BodyVelocity.Parent = Character
			v3.Parent = Character
			v10:Stop()
			v11:Stop()
		end
	end
end)
