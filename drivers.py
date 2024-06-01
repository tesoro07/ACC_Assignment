import wmi
import datetime


def convert_to_datetime(wmi_date):
    """Convert WMI datetime string to a Python datetime object, handling cases where the date might be missing."""
    try:
        if wmi_date:
            return datetime.datetime.strptime(wmi_date.split('.')[0], '%Y%m%d%H%M%S')
    except Exception as e:
        return None
    return None


def get_pnp_signed_drivers(conn):
    print("PnP Signed Drivers:")
    for driver in conn.Win32_PnPSignedDriver():
        install_date = convert_to_datetime(driver.InstallDate)
        install_date_str = install_date.strftime('%Y-%m-%d %H:%M:%S') if install_date else "Not Available"
        print(f"Device Name: {driver.DeviceName}")
        print(f"Driver Version: {driver.DriverVersion}")
        print(f"Friendly Name: {driver.FriendlyName}")
        print(f"INF Name: {driver.InfName}")
        print(f"Install Date: {install_date_str}")
        print(f"Is Signed: {driver.IsSigned}")
        print(f"Location: {driver.Location}")
        print(f"Manufacturer: {driver.Manufacturer}")
        print(f"Name: {driver.Name}")
        print(f"PDO: {driver.PDO}")
        print(f"Driver Provider Name: {driver.DriverProviderName}")
        print(f"Signer: {driver.Signer}")
        print(f"Started: {driver.Started}")
        print(f"Start Mode: {driver.StartMode}")
        print(f"Status: {driver.Status}")
        print(f"System Creation Class Name: {driver.SystemCreationClassName}")
        print(f"System Name: {driver.SystemName}")
        print(" ")
        print("########################################################################################")


def get_system_drivers(conn):
    print("System Drivers:")
    for driver in conn.Win32_SystemDriver():
        install_date = convert_to_datetime(driver.InstallDate)
        install_date_str = install_date.strftime('%Y-%m-%d %H:%M:%S') if install_date else "Not Available"
        print(f"Name: {driver.Name}")
        print(f"Description: {driver.Description}")
        print(f"Display Name: {driver.DisplayName}")
        print(f"Error Control: {driver.ErrorControl}")
        print(f"Install Date: {install_date_str}")
        print(f"Path Name: {driver.PathName}")
        print(f"Service Type: {driver.ServiceType}")
        print(f"Started: {driver.Started}")
        print(f"Start Mode: {driver.StartMode}")
        print(f"Start Name: {driver.StartName}")
        print(f"State: {driver.State}")
        print(f"Status: {driver.Status}")
        print(f"System Creation Class Name: {driver.SystemCreationClassName}")
        print(f"System Name: {driver.SystemName}")
        print(f"Tag ID: {driver.TagId}")
        print(" ")
        print("########################################################################################")


def main():
    conn = wmi.WMI()
    get_pnp_signed_drivers(conn)
    print("\n\n")
    get_system_drivers(conn)


if __name__ == "__main__":
    main()
