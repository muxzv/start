--//Datastore Script:

--//Datastore
local DataStoreService = game:GetService("DataStoreService") --Gets the DataStoreService
local dataStore = DataStoreService:GetDataStore("Test") --Gives the Datastore a name

--//Function
local function saveData(player) --Create out own function for saving data
	local tableToSave = { --Creates a table for our values
		player.leaderstats.Money.Value; --Saves the first value
	} --You can continue the list in the same order by adding "player.leaderstats.IntValueName.Value;"

	local success, errorMessage = pcall(dataStore.SetAsync, dataStore, player.UserId, tableToSave) --Checks if datastore succeeded

	if success then --If datastore success then
		print("Data has been saved!") --Prints success
	else --If datastore fails then
		print("Data has not been saved!") --Prints failure
	end
end

--//leaderstats
game.Players.PlayerAdded:Connect(function(player) --When a player joins the game
	player.CharacterAdded:Wait() --Wait for the player to load
	local leaderstats = Instance.new("Folder") --Creates a new folder for the player
	leaderstats.Name = "leaderstats" --Sets Folder name to "leaderstats" --MAKE SURE YOU DON'T CHANGE THIS
	leaderstats.Parent = player --Puts the Folder under the player

	local points = Instance.new("IntValue") --Creates an IntValue
	points.Name = "Money" --Sets IntValue name to "Points" (If you change this make sure you change all of them)
	points.Parent = leaderstats --Puts the IntValue under the "leaderstats" folder
	points.Value = 321 --Gives the IntValue Value to start off with

	local data = nil --Data is empty

	local success, errorMessage = pcall(function() 
		data = dataStore:GetAsync(player.UserId) --Finds the player's UserId and data
	end)

	if success and data then --If UserId and Data found then
		points.Value = data[1] --Sets points to the first set of data
	else --If UserId or Data not found then
		print("The Player has no Data!") --Player has no data
		warn(errorMessage)
	end
end)

game.Players.PlayerRemoving:Connect(function(player) --When player is leaving the game
	saveData(player) --Save the player's data
end)

game:BindToClose(function() --When the game's servers are shutting down
	for _, player in ipairs(game.Players:GetPlayers()) do --loop through all the players in the server
		task.spawn(saveData, player) --save all the player's data
	end
end)
