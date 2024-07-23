-- Script ChangeAnimations in ServerScriptService

local Players = game:GetService("Players")
local runAnimation = "rbxassetid://18618439306" -- replace these with your own animation ids
local JumpAnimation = "rbxassetid://18618443642" -- replace these with your own animation ids

local function onCharacterAdded(character)
	local humanoid = character:WaitForChild("Humanoid")
	local animateScript = character:WaitForChild("Animate")
	
	animateScript.run.RunAnim.AnimationId = runAnimation
	animateScript.jump.JumpAnim.AnimationId = JumpAnimation
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
