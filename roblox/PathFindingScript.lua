
--{{ SERVICES }}--
local Players = game:GetService("Players")
local PathfindingService = game:GetService("PathfindingService")

--{{ VARIABLES }}--
local rig = script.Parent
--{{ FUNCTIONS }}--
local function checkForCharacter(character)
	local rayOrigin = rig:FindFirstChild("HumanoidRootPart").Position
	local rayDirection = (character.HumanoidRootPart.Position - rayOrigin).Unit * 40
	
	local raycastResult = workspace:Raycast(rayOrigin, rayDirection, RaycastParams.new())
	
	if raycastResult then
		local raycastInstance = raycastResult.Instance
		if raycastInstance:IsDescendantOf(character) then
			return true
		end
	else
		return false
	end
end

local function findNearestPlayer()
	local players = Players:GetPlayers()
	local nearestPlayer = nil
	local maxDistance = 40
	
	for _, player in pairs(players) do
		if player.Character ~= nil then
			local targetCharacter = player.Character
			local distance = (rig.HumanoidRootPart.Position - targetCharacter.HumanoidRootPart.Position).Magnitude
		
			if distance < maxDistance and checkForCharacter(targetCharacter) then
				nearestPlayer = targetCharacter
				maxDistance = distance
			end
		end
	end
	return nearestPlayer
end

local function attack(character)
	local distance = (rig.HumanoidRootPart.Position - character.HumanoidRootPart.Position).Magnitude
	
	if distance > 8 then
		rig.Humanoid:MoveTo(character.HumanoidRootPart.Position)
	else
		character.Humanoid.Health = 0
		script.Parent.Monster:Play()
		wait(2.5)
		script.Parent.Monster:Stop()

	end
end

local function calculatePath(destination)
	local agentParams = {
		["AgentHeight"] = 5.5,
		["AgentRadius"] = 4,
		["AgentCanJump"] = false
	}
	
	local path = PathfindingService:CreatePath(agentParams)
	path:ComputeAsync(rig.HumanoidRootPart.Position, destination)
	return path
end

local function walkToDestination(destination)
	local path = calculatePath(destination)
	
	if path.Status == Enum.PathStatus.Success then
		for _, waypoint in pairs(path:GetWaypoints()) do
			local nearestPlayer = findNearestPlayer()
			if nearestPlayer then
				attack(nearestPlayer)
				break
			else
				rig.Humanoid:MoveTo(waypoint.Position)
				rig.Humanoid.MoveToFinished:Wait()
			end
		end
	else
		rig.Humanoid:MoveTo(destination - (rig.HumanoidRootPart.CFrame.LookVector * 10))
	end
end

local function patrol()
	local waypoints = workspace.Waypoints:GetChildren()
	local randomNumber = math.random(1, #waypoints)

	walkToDestination(waypoints[randomNumber].Position)
end

while task.wait(1) do
	patrol()
end
