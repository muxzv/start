local minHeight = 10
local maxHeight = 30

game.Players.PlayerAdded:Connect(function(player)
	player.CharacterAdded:Connect(function(character)

		local humanoid = character:WaitForChild("Humanoid")
		local humanoidRootPart = character:WaitForChild("HumanoidRootPart")
		local playerHeight

		if humanoid and humanoidRootPart then
			wait(1)
			humanoid.FreeFalling:Connect(function(newState)
				if newState then
					playerHeight = humanoidRootPart.Position.Y
				elseif not newState then
					local fallHeight = playerHeight - humanoidRootPart.Position.Y

					if fallHeight >= maxHeight then
						humanoid.Health = 0
					elseif fallHeight >= minHeight then
						humanoid.Health = humanoid.Health - math.floor(fallHeight)
					end
				end
			end)
		end 

	end)
end)
