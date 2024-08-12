local JumpscareEvent = game.ReplicatedStorage.RemoveEvents.JumpscareEvent

script.Parent.Touched:Connect(function(Hit)
	if Hit.Parent:FindFirstChild("Humanoid") then
		local Player = game.Players:GetPlayerFromCharacter(Hit.Parent)
		JumpscareEvent:FireClient(Player)
		--script.Parent:Destroy()
	end
end)
