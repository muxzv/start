--[[ Made by coolcapidog
Channel ->> https://www.youtube.com/c/coolcapidog
You can change the settings but you shouldn't change anything except settings.
]]
------------------------------------ Settings
local BloodDelay = 10
local BloodPerHit = 4
------------------------------------ Settings

local tweenService = game:GetService("TweenService")
local Players = game:GetService("Players")

local tweenPartSize = function(part, duration, direction, size)
    local tween = tweenService:Create(part, TweenInfo.new(duration, Enum.EasingStyle.Sine, direction), {Size = size})
    tween:Play()
    return tween
end
local createBlood = function(position)
    local randomSize = math.random(2, 20) / 10
	local bloodClone = script:WaitForChild("Blood"):Clone()
    bloodClone.Position = position + Vector3.new(0, 0.05, 0)
    bloodClone.Size = Vector3.new(randomSize, 0.1, randomSize)
    bloodClone.Parent = game.Workspace.BloodFolder
    if math.random(2) == 1 then
        bloodClone.Sound:Play()
    end
    return bloodClone
end
local expandBlood = function(part)
    local randomIncrement = math.random(5, 10) / 10
    local tween = tweenPartSize(part, 5, Enum.EasingDirection.Out, Vector3.new(part.Size.X + randomIncrement, 0.1, part.Size.Z + randomIncrement))
    spawn(function()
        tween.Completed:Wait()
        tween:Destroy()
    end)
end
local deleteBlood = function(part)
    local tween = tweenPartSize(part, 0.5, Enum.EasingDirection.In, Vector3.new(0, 0.1, 0))
    spawn(function()
        tween.Completed:Wait()
        tween:Destroy()
        part:Destroy()
    end)
end
local raycast = function(character, raycastOrigin, raycastDirection)
    local params = RaycastParams.new()
	params.FilterDescendantsInstances = {character, game.Workspace.BloodFolder}
    params.FilterType = Enum.RaycastFilterType.Blacklist
    params.IgnoreWater = true
    local raycastResult = workspace:Raycast(raycastOrigin, raycastDirection, params)
    if raycastResult then
        return raycastResult
    end
end
Players.PlayerAdded:Connect(function(plr)
	plr.CharacterAdded:Connect(function(character)
        local rootPart = character:WaitForChild("HumanoidRootPart")
        local humanoid = character:WaitForChild("Humanoid")
        local oldHealth = humanoid.Health
		local particlesClone = script:WaitForChild("Particles"):Clone()
        particlesClone.Parent = rootPart
        humanoid.HealthChanged:Connect(function(health)
            if health < oldHealth then
                oldHealth = health
                spawn(function()
					for i = 1, BloodPerHit do
                        local raycastOrigin = rootPart.Position + Vector3.new(math.random(-20, 20) / 10, 0, math.random(-20, 20) / 10)
                        local raycastDirection = Vector3.new(0, -8, 0)
                        local raycastResult = raycast(character, raycastOrigin, raycastDirection)
                        if raycastResult then
                            particlesClone:Emit(2)
                            delay(0.5, function()
                                local newBlood = createBlood(raycastResult.Position)
                                expandBlood(newBlood)
                                delay(BloodDelay, function()
                                    deleteBlood(newBlood)
                                end)
                            end)
                        end
                        wait(math.random(0.5, 2) / 10)
                    end
                end)
            else
                oldHealth = health
            end
        end)
    end)
end)
