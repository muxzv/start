local db = true
script.Parent.Touched:Connect(function(hit)
	if hit.Parent:FindFirstChild("Humanoid") ~= nil then
		if db then
			db = false
			script.Parent.Transparency =1
			local player = game.Players:GetPlayerFromCharacter(hit.Parent)
			player.leaderstats.Money.Value = player.leaderstats.Money.Value +1
			script.sound:play()
			script.Parent.Transparency = 1
			wait(5)
			db = true
			script.Parent.Transparency = 0
		end
	end
end)
