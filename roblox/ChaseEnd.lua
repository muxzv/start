local monster = script.Parent.Parent.Monster

script.Parent.Touched:Connect(function(hit)
	if hit and hit.Parent:FindFirstChild("Humanoid") then
		monster:Destroy()
	end
end)
