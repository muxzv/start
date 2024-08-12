script.Parent.Touched:Connect(function(hit)
	if hit and hit.Parent:FindFirstChild("Humanoid") then
		script.Parent:Destroy(  )
		game.ReplicatedStorage.Jumpscare.Parent = game.Workspace
		wait(0.5)
		game.Workspace.Jumpscare.Parent = game.ReplicatedStorage
	end
end) 
