# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 20:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.43% | 3098.2 | 10206.7 | 1000ms | 110/385 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 121.8 | 3806.8 | 1500ms | 1/385 |
| ❌ | `nasa_apod` | 63.64% | 40.0% | 4120.0 | 10538.0 | 2000ms | 231/385 |
| ❌ | `ipapi_check` | 93.77% | 100.0% | 159.6 | 353.0 | 2500ms | 0/385 |
| ⚠️ | `open_meteo_weather` | 97.92% | 96.88% | 754.1 | 14877.1 | 2000ms | 12/385 |
| ⚠️ | `dog_ceo_random` | 99.22% | 89.09% | 915.4 | 10244.1 | 2500ms | 42/385 |
| ✅ | `useless_fact` | 99.48% | 98.96% | 588.8 | 10229.6 | 2500ms | 4/385 |
| ✅ | `catfact_random` | 99.48% | 99.74% | 245.4 | 10070.5 | 3000ms | 1/385 |
| ✅ | `agify_name` | 100.0% | 99.74% | 372.8 | 3237.1 | 2000ms | 1/385 |
| ✅ | `rest_countries` | 100.0% | 98.96% | 262.2 | 7269.1 | 2500ms | 4/385 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 235.0 | 2314.9 | 2000ms | 1/385 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/385 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 17:00 | 5580.9 | 69.57% |
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `nasa_apod` | 18:00 | 5312.9 | 81.25% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 20:00 | 4613.0 | 65.38% |
| `nasa_apod` | 14:00 | 4584.8 | 60.87% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |
| `nasa_apod` | 13:00 | 4333.9 | 66.67% |
| `nasa_apod` | 21:00 | 4275.9 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
