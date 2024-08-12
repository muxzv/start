script.Parent.Touched:Connect(function(hit)
	if hit and hit.Parent:FindFirstChild("Humanoid") then
	 hit.Parent.Humanoid.Health = hit.Parent.Humanoid.Health - 50
	end
end)
