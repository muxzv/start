script.Parent.Touched:Connect(function(hit)
	if hit and hit.Parent:FindFirstChild("Humanoid") then
		script.Parent.Parent.thing.Anchored = false
		script.Parent.Parent.thing.Transparency = 0
	end
end)
