local Character = script.Parent
wait(1)
 
Character.Humanoid.Died:connect(function()
	for i, tool in pairs(Character:GetChildren()) do
		if tool:IsA("Tool") then
			tool.Parent = game.Workspace
		end
	end
	if game.Players[script.Parent.Name]:FindFirstChild("Backpack") then
		for i, tool in pairs(game.Players[script.Parent.Name].Backpack:GetChildren()) do
			tool.Parent = game.Workspace
		end
	end
end)
