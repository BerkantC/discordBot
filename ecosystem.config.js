module.exports = {
  apps : [{
    name   : "Bonker",
    script : "./bonker/bonker.py",
    watch: true,
    env: {
	"PYTHONPATH": ":discordBot",
    }
  }]
}
