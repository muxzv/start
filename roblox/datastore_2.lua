local db = true --debounce

script.Parent.Touched:Connect(function(hit) --When something touches the part, the script runs
	if hit and hit.Parent:FindFirstChild("Humanoid") then --Checks if a character touched the part
		if db == true then --If debounce then
			db = false --Sets debounce to false
			local player = game.Players:GetPlayerFromCharacter(hit.Parent) --If character then it will get the player using the character
			local leaderstats = player.leaderstats --Gets the player's leaderstats
			leaderstats.Money.Value += 5 --Adds 5 points to the player
			task.wait(2) --Cooldown timer, change the number in brakets to how many seconds you want the cooldown to be
			db = true --Sets debounce to true
		end
	end
end)
