import subprocess

discover_output = subprocess.run(['yts','discover'], stdout=subprocess.PIPE)
tstr=discover_output.stdout.decode('utf-8')
se = tstr.split("\n")
print('Running test on : ' + se[1])
deviceId = se[1][1:3]

runtest_output = subprocess.run(['yts','test',deviceId,'EME Conformance Tests Widevine WidevineH264Video'], stdout=subprocess.PIPE)
log = runtest_output.stdout.decode('utf-8')
print(log)
