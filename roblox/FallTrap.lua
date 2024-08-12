local part = script.Parent
part.Touched:Connect(function(hit)
	if hit.Parent:FindFirstChild("Humanoid") then
		part.Anchored = false
	end
end)
