script.Parent.Touched:Connect(function(hit)
	if game.Players:GetPlayerFromCharacter(hit.Parent) then
		if script.Parent.Locked == false and script.Parent.Parent.Teleport2.Locked == false then
			script.Parent.Locked = true
			script.Parent.Parent.Teleport2.Locked = true
			hit.Parent:MoveTo(workspace.Teleport2.Position)
			wait(1)
			script.Parent.Locked = false
			script.Parent.Parent.Teleport2.Locked = false
		end
	end
end)
