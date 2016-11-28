_Buffer = {
	_init_(max_wip=7, max_flow=3) {
		this.queued = 0
		this.wip = 0
		this.max_wip = max_wip
		this.max_flow = max_flow
	}
	,
	work(u) {
		u = Math.max(0, parseInt(Math.round(u)))
		u = min(u, this.max_wip)
		this.wip += u

		r = getRandomInt(0, this.wip)
		this.wip -= r
		this.queued += r

		r = getRandomInt(0, this.max_flow)
		r = Math.min(r, this.queued)
		this.queued -= r

		return this.queued
	}
}

_Controller = {
	_init_(kp, ki) {
		this.kp, this.ki = kp, ki
		this.I = 0
	}
	,
	work(e) {
		this.I += e

		return (this.kp * e) + (this.ki * this.i)
	}
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

function open_loop(p, tm=5000) {
	function target(t) {
		return 5.0
	}

	for (t in range(tm)) {
		u = target(t)
		y = p.work(u)

		console.log(t,u,0,u,y)
	}
}

function closed_loop(c, p, tm=5000) {
	function setpoint(t) {
		if (t < 100) return 0

		if (t < 300) return 50

		return 10
	}

	y = 0

	for (t in range(tm))
}