FROM ciai-docker-stable-local.artifactory-na.honeywell.com/windows/servercore:1809
WORKDIR C:\\install
ADD https://dl.influxdata.com/telegraf/releases/telegraf-1.12.3_windows_amd64.zip C:\\install\\telegraf.zip
RUN powershell -Command Expand-Archive 'C:\\install\\telegraf.zip' 'C:\\install\\';
RUN Powershell.exe -Command New-LocalUser -Name telegraf -NoPassword -AccountNeverExpires ; \
                   Set-LocalUser telegraf -PasswordNeverExpires 1; \
                   Add-LocalGroupMember -Group "Administrators" -Member "telegraf";
USER telegraf
COPY telegraf.conf "c:\\install\\telegraf\\telegraf.conf"
ENTRYPOINT ["C:\\install\\telegraf\\telegraf.exe"]
CMD [" --config C:\\install\\telegraf\\telegraf.conf"]
